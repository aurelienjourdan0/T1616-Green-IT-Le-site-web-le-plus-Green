from flask import Flask, render_template

app = Flask(__name__)

# Page d'accueil
@app.route('/')
def home():
    return render_template('home.html')

# Détails d'un jeu
@app.route('/details/<string:jeu_name>')
def details(jeu_name):
    # Exemple de données à remplacer par ta base de données
    jeu = {
        'name': jeu_name,
        'yearpublished': 2000,
        'minplayers': 2,
        'maxplayers': 4,
        'playingtime': 60,
        'minage': 10,
        'average': 7.4,
        'bayes_average': 7.2,
        'users_rated': 1500,
        'description': 'Un jeu captivant entre stratégie et chance.',
        'thumbnail': jeu_name,  # On ne met que le nom de l'image sans le chemin
        'boardgamecategory': ['Stratégie', 'Famille'],
        'boardgamepublisher': 'Z-Man Games'
    }
    return render_template('details.html', jeu=jeu)

# Page des événements
@app.route('/events')
def events():
    return render_template('events.html')

# Page du forum
@app.route('/forum')
def forum():
    return render_template('forum.html')

@app.route('/forum/post/<int:post_id>')
def forum_post(post_id):
    # Exemple de données à remplacer par une vraie base de données
    post = {
        'id': post_id,
        'title': f"Sujet #{post_id}",
        'content': "Voici le contenu détaillé du sujet...",
        'author': "Utilisateur 1",
        'date_posted': "2025-04-08"
    }
    # Exemple de données, incluant un post "faux"
    if post_id == 1:
        post = {
            'id': 1,
            'title': "Vente de jeux de société - Offre spéciale!",
            'content': "Des jeux en vente à moitié prix. Contactez-nous pour plus d'infos.",
            'author': "Utilisateur A",
            'date_posted': "2025-04-08"
        }

    # Rendre la page avec les détails du post
    return render_template('forum_post.html', post=post)


@app.route('/submit_forum_post', methods=['POST'])
def submit_forum_post():
    title = request.form['title']
    content = request.form['content']
    
    # Ici, tu pourrais enregistrer ces données dans une base de données.
    # Exemple : forum_db.save(title=title, content=content)
    
    return redirect(url_for('forum'))  # Redirige vers le forum après avoir soumis


if __name__ == '__main__':
    app.run(debug=True)
