import pandas as pd
import numpy as np
import pymysql

# Connexion MySQL locale
#connection = pymysql.connect(
#    host='localhost',
#    user='root',
#    password='aqwpm82295',
#    database='details',
#    charset='utf8mb4',
#    cursorclass=pymysql.cursors.Cursor
#)

# Connexion MySQL PythonAnywhere
connection = pymysql.connect(
    host='EnJeuxLudiques.mysql.pythonanywhere-services.com',  # Utilise ton username pour la partie host
    user='EnJeuxLudiques',  # Remplace par ton username PythonAnywhere
    password='aqwpm82295',  # Remplace par ton mot de passe PythonAnywhere
    database='EnJeuxLudiques$default',  # Nom complet de ta base
    charset='utf8mb4'
)

cursor = connection.cursor()

# ----------------------
# Création des tables normalisées
# ----------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS game (
    id INT PRIMARY KEY,
    name VARCHAR(511) NOT NULL,
    description TEXT,
    yearpublished INT,
    minplayers INT,
    maxplayers INT,
    playingtime INT,
    minplaytime INT,
    maxplaytime INT,
    minage INT,
    owned INT DEFAULT 0,
    trading INT DEFAULT 0,
    wanting INT DEFAULT 0,
    wishing INT DEFAULT 0
);
""")

# Tables principales pour entités
entities = ["category", "mechanic", "family", "expansion", "implementation", "designer", "artist", "publisher"]
for entity in entities:
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {entity} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) UNIQUE
    );
    """)

# Tables de liaison
for entity in entities:
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS game_{entity} (
        game_id INT NOT NULL,
        {entity}_id INT NOT NULL,
        FOREIGN KEY (game_id) REFERENCES game(id) ON DELETE CASCADE,
        FOREIGN KEY ({entity}_id) REFERENCES {entity}(id) ON DELETE CASCADE
    );
    """)

cursor.execute("""
CREATE TABLE IF NOT EXISTS rating (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    `rank` INT,
    average FLOAT NOT NULL,
    bayes_average FLOAT NOT NULL,
    users_rated INT NOT NULL,
    url VARCHAR(200),
    thumbnail VARCHAR(255)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS user (
    id SERIAL PRIMARY KEY,
    username VARCHAR(150) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    date_inscription TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    role ENUM('user', 'admin') DEFAULT 'user'
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS comment (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    game_id INTEGER REFERENCES game(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES user(id) ON DELETE CASCADE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS event (
    id SERIAL PRIMARY KEY,
    name_event VARCHAR(255) NOT NULL,
    date TIMESTAMP NOT NULL,
    lieu VARCHAR(255) NOT NULL,
    description TEXT,
    user_id INTEGER REFERENCES user(id) ON DELETE SET NULL
);
""")

connection.commit()

# ----------------------
# Chargement et nettoyage des CSV
# ----------------------

details_df = pd.read_csv('details.csv', sep=';', encoding='latin1', low_memory=False)
ratings_df = pd.read_csv('ratings.csv', sep=';', encoding='latin1')

def safe_int(x):
    try:
        return int(float(x))
    except (ValueError, TypeError):
        return None

int_columns = [
    'yearpublished', 'minplayers', 'maxplayers', 'playingtime', 
    'minplaytime', 'maxplaytime', 'minage', 'owned', 'trading', 'wanting', 'wishing'
]
for col in int_columns:
    details_df[col] = details_df[col].apply(safe_int)


# Fonction pour parser les colonnes de type liste
def parse_list_column(cell):
    if pd.isna(cell) or cell.strip() == "":
        return []
    return [item.strip().strip("'").strip('"') for item in cell.strip("[]").split(';')]

# Appliquer aux colonnes concernées
list_columns = {
    'boardgamecategory': 'category',
    'boardgamemechanic': 'mechanic',
    'boardgamefamily': 'family',
    'boardgameexpansion': 'expansion',
    'boardgameimplementation': 'implementation',
    'boardgamedesigner': 'designer',
    'boardgameartist': 'artist',
    'boardgamepublisher': 'publisher'
}

for col in list_columns:
    details_df[col] = details_df[col].apply(parse_list_column)


details_df = details_df.replace({np.nan: None})
ratings_df = ratings_df.replace({np.nan: None})

# ----------------------
# Insérer les données uniques dans chaque table principale
# ----------------------
def insert_unique_values(column_name, table_name):
    unique_values = set()
    for row in details_df[column_name]:
        unique_values.update(row)
    for value in unique_values:
        if value:
            cursor.execute(f"INSERT IGNORE INTO {table_name} (name) VALUES (%s)", (value,))

for df_col, table in list_columns.items():
    insert_unique_values(df_col, table)

# ----------------------
# Insérer les gamex dans 'game'
# ----------------------
for _, row in details_df.iterrows():
    cursor.execute("""
        INSERT INTO game (
            id, name, description, yearpublished, minplayers, maxplayers, playingtime,
            minplaytime, maxplaytime, minage, owned, trading, wanting, wishing
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['id'], row['primary'], row['description'], row['yearpublished'],
        row['minplayers'], row['maxplayers'], row['playingtime'],
        row['minplaytime'], row['maxplaytime'], row['minage'],
        row['owned'], row['trading'], row['wanting'], row['wishing']
    ))

# ----------------------
# Remplir les tables d'association (game_...)
# ----------------------
def link_game_to_elements(df_column, lookup_table, link_table):
    for _, row in details_df.iterrows():
        for item in row[df_column]:
            if item:
                cursor.execute(f"SELECT id FROM {lookup_table} WHERE name = %s", (item,))
                result = cursor.fetchone()
                if result:
                    element_id = result[0]
                    cursor.execute(
                        f"INSERT INTO {link_table} (game_id, {lookup_table}_id) VALUES (%s, %s)",
                        (row['id'], element_id)
                    )

for df_col, table in list_columns.items():
    link_game_to_elements(df_col, table, f"game_{table}")

# ----------------------
# Insérer les rating
# ----------------------
for _, row in ratings_df.iterrows():
    cursor.execute("""
        INSERT INTO rating (id, name, year, `rank`, average, bayes_average, users_rated, url, thumbnail)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['id'], row['name'], row['year'], row['rank'], row['average'],
        row['bayes_average'], row['users_rated'], row['url'], row['thumbnail']
    ))

connection.commit()
