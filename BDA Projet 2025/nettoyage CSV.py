
# ----------------------
# Chargement et nettoyage des CSV
# ----------------------


def add_quote_after_third_semicolon(line):
    semicolon_indices = [i for i, c in enumerate(line) if c == ';']
    
    # S'assurer qu'il y a au moins 3 points-virgules
    if len(semicolon_indices) >= 3:
        third_index = semicolon_indices[2]
        
        # Vérifie s'il y a déjà un guillemet après le troisième point-virgule
        after_third = line[third_index + 1:]
        if '"' not in after_third:
            # Insère le guillemet après le troisième point-virgule
            line = line[:third_index + 1] + '"' + line[third_index + 1:]
            print(f"Ajout de guillemet après le troisième point-virgule dans la ligne : {line.strip()}")
    return line

def clean_line(line):
    line = add_quote_after_third_semicolon(line)
    return line.strip()

cleaned_lines = []
with open('details.csv', 'r', encoding='latin1') as f:
    for i, line in enumerate(f):
        if i == 0:
            cleaned_lines.append(line)  # Ne rien faire sur la première ligne
        else:
            cleaned = clean_line(line)
            cleaned_lines.append(cleaned)

        
# Sauvegarder dans un fichier temporaire
with open('details_cleaned.csv', 'w', encoding='latin1') as f:
    for line in cleaned_lines:
        f.write(line + '\n')

details_df = pd.read_csv('details_cleaned.csv', sep=';', encoding='latin1', low_memory=False)
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

details_df = details_df.replace({np.nan: None})
ratings_df = ratings_df.replace({np.nan: None})

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
