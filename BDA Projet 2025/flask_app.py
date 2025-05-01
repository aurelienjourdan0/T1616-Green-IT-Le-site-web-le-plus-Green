from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
from sqlalchemy.sql.expression import func, or_, and_
from datetime import datetime, timezone


pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.secret_key = 'secret_key_change_me'

# Configuration de la base de données
import os

# Si tu es sur PythonAnywhere, configure la base de données avec les détails de production
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://EnJeuxLudiques:aqwpm82295@EnJeuxLudiques.mysql.pythonanywhere-services.com/EnJeuxLudiques$default'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:aqwpm82295@localhost/details'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# ----------- TABLES PRINCIPALES -----------

class Artist(db.Model):
    __tablename__ = 'artist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)


class Designer(db.Model):
    __tablename__ = 'designer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)


class Expansion(db.Model):
    __tablename__ = 'expansion'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)


class Family(db.Model):
    __tablename__ = 'family'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)


class Game(db.Model):
    __tablename__ = 'game'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    yearpublished = db.Column(db.Integer)
    minplayers = db.Column(db.Integer)
    maxplayers = db.Column(db.Integer)
    playingtime = db.Column(db.Integer)
    minplaytime = db.Column(db.Integer)
    maxplaytime = db.Column(db.Integer)
    minage = db.Column(db.Integer)
    categories = db.relationship('Category', secondary='game_category', backref='games')


class Implementation(db.Model):
    __tablename__ = 'implementation'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)


class Mechanic(db.Model):
    __tablename__ = 'mechanic'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)


class Publisher(db.Model):
    __tablename__ = 'publisher'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)


class Rating(db.Model):
    __tablename__ = 'rating'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer)
    rank = db.Column('rank', db.Integer)
    average = db.Column(db.Float)
    bayes_average = db.Column(db.Float)
    users_rated = db.Column(db.Integer)
    url = db.Column(db.String(200))
    thumbnail = db.Column(db.String(255))


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.Text, nullable=False)
    date_inscription = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    role = db.Column(db.String(50))

    # Relations
    comments = db.relationship('Comment', back_populates='user', cascade='all, delete-orphan')
    events = db.relationship('Event', back_populates='user', cascade='all, delete-orphan')


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    game = db.relationship('Game', backref='comments')
    user = db.relationship('User', back_populates='comments')


class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    name_event = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    lieu = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship('User', back_populates='events')


# ----------- TABLES ASSOCIATIVES -----------

class GameArtist(db.Model):
    __tablename__ = 'game_artist'
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), primary_key=True)


class GameCategory(db.Model):
    __tablename__ = 'game_category'
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), primary_key=True)


class GameDesigner(db.Model):
    __tablename__ = 'game_designer'
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), primary_key=True)
    designer_id = db.Column(db.Integer, db.ForeignKey('designer.id'), primary_key=True)


class GameExpansion(db.Model):
    __tablename__ = 'game_expansion'
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), primary_key=True)
    expansion_id = db.Column(db.Integer, db.ForeignKey('expansion.id'), primary_key=True)


class GameFamily(db.Model):
    __tablename__ = 'game_family'
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), primary_key=True)
    family_id = db.Column(db.Integer, db.ForeignKey('family.id'), primary_key=True)


class GameImplementation(db.Model):
    __tablename__ = 'game_implementation'
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), primary_key=True)
    implementation_id = db.Column(db.Integer, db.ForeignKey('implementation.id'), primary_key=True)


class GameMechanic(db.Model):
    __tablename__ = 'game_mechanic'
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), primary_key=True)
    mechanic_id = db.Column(db.Integer, db.ForeignKey('mechanic.id'), primary_key=True)


class GamePublisher(db.Model):
    __tablename__ = 'game_publisher'
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), primary_key=True)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'), primary_key=True)


# ----------- ROUTES -----------

@app.route('/')
def home():
    top_3 = db.session.query(Rating).order_by(Rating.rank).limit(3).all()
    random_5 = db.session.query(Rating).order_by(func.rand()).limit(5).all()
    return render_template('home.html', top_3=top_3, random_5=random_5)

@app.route('/details/<string:game_name>')
def details(game_name):
    game = Game.query.filter_by(name=game_name).first()
    rating = Rating.query.filter_by(name=game_name).first()

    if game and rating:
        return render_template('details.html', game=game, rating=rating)
    else:
        return "game non trouvé", 404

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/forum')
def forum():
    posts = [
        {'id': 1, 'title': 'Vente de jeux de société - Offre spéciale!', 'author': 'user A', 'date_posted': '2025-04-08'},
        {'id': 2, 'title': 'Recherche de jeux coopératifs', 'author': 'user B', 'date_posted': '2025-04-07'},
        {'id': 3, 'title': 'Événements autour des jeux de société', 'author': 'user C', 'date_posted': '2025-04-06'}
    ]
    return render_template('forum.html', posts=posts)

@app.route('/forum/post/<int:post_id>')
def forum_post(post_id):
    post = {
        'id': post_id,
        'title': f"Sujet #{post_id}",
        'content': "Bonjour, je vends des jeux de société super rare qui s'appelle \"Bazaar\" et \"Virdigo\" ! Contactez moi je les vends à moins de 10 euros !",
        'author': "Aurélien Jourdan",
        'date_posted': "2025-04-08"
    }
    return render_template('forum_post.html', post=post)

@app.route('/submit_forum_post', methods=['POST'])
def submit_forum_post():
    title = request.form['title']
    content = request.form['content']
    return redirect(url_for('forum'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        # On remet à 1 si c'est une soumission manuelle (nouvelle recherche)
        page = 1
        selected_genre = request.form.get('genre', '')
        selected_year = request.form.get('year', '')
        selected_players = request.form.get('players', '')
        keyword = request.form.get('keyword', '')
        per_page = int(request.form.get('per_page', 10))
    else:
        # Navigation via pagination
        page = int(request.args.get('page', 1))
        selected_genre = request.args.get('genre', '')
        selected_year = request.args.get('year', '')
        selected_players = request.args.get('players', '')
        keyword = request.args.get('keyword', '')
        per_page = int(request.args.get('per_page', 10))

    # Filtres disponibles
    years = sorted({g.yearpublished for g in Game.query.distinct(Game.yearpublished).all() if g.yearpublished})
    genres = [c.name for c in Category.query.order_by(Category.name).all()]

    # Construction de la requête
    query = Game.query

    if selected_genre:
        query = query.join(GameCategory).join(Category).filter(Category.name.ilike(f"%{selected_genre}%"))
    if selected_year:
        query = query.filter(Game.yearpublished == int(selected_year))
    if selected_players:
        try:
            nb = int(selected_players)
            query = query.filter(and_(Game.minplayers <= nb, Game.maxplayers >= nb))
        except ValueError:
            if selected_players == "5+":
                query = query.filter(Game.maxplayers >= 5)
    if keyword:
        query = query.filter(Game.name.ilike(f"%{keyword}%"))

    # Pagination
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    game = pagination.items

    # Récupération des ratings
    ratings = Rating.query.filter(Rating.name.in_([g.name for g in game])).all()
    rating_map = {r.name: r for r in ratings}

    return render_template(
        'search.html',
        game=game,
        years=years,
        genres=genres,
        selected_genre=selected_genre,
        selected_year=selected_year,
        selected_players=selected_players,
        keyword=keyword,
        rating_map=rating_map,
        per_page=per_page,
        pagination=pagination
    )



# ----------- AUTHENTIFICATION -----------

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Nom d'utilisateur déjà pris.")
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Compte créé. Vous pouvez maintenant vous connecter.")
        return redirect(url_for('login'))
    
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash("Connexion réussie.")
            return redirect(url_for('home'))
        else:
            flash("Identifiants incorrects.")
    
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    flash("Déconnecté avec succès.")
    return redirect(url_for('home'))


# Test DB
@app.route('/check_db')
def check_db():
    try:
        game = Game.query.first()
        return f"✅ Connexion réussie : {game.name}" if game else "✅ Connexion OK, mais base vide."
    except Exception as e:
        return f"❌ Erreur : {e}"

@app.route('/check_rating')
def check_rating():
    try:
        rating = Rating.query.first()
        return f"✅ Connexion rating OK : {rating.name}" if rating else "✅ rating vide."
    except Exception as e:
        return f"❌ Erreur rating : {e}"

if __name__ == '__main__':
    app.run(debug=True)
