T1616-Green-IT-Le-site-web-le-plus-Green
Objectif :
Concevoir, implémenter et analyser l'empreinte carbone d'un site web. Le but est de créer un site web aussi écologique que possible, en minimisant son impact environnemental tout en conservant une utilité concrète pour l'utilisateur.

Instruction pour cloner, configurer et exécuter le projet :
Cloner le dépôt :

git clone https://github.com/aurelienjourdan0/T1616-Green-IT-Le-site-web-le-plus-Green.git
cd enjeuxludiques
Créer un environnement virtuel (optionnel mais recommandé) :
python -m venv env
source env/bin/activate  # ou `env\Scripts\activate` sous Windows
Installer les dépendances :

pip install -r requirements.txt
Lancer l’application localement :

flask run

Accéder au site :

Ouvrir un navigateur et aller sur http://127.0.0.1:5000/

Configuration de la base de données (si nécessaire) :

Importer le fichier SQL fourni dans un serveur MySQL local ou distant.

Modifier les variables d’environnement ou le fichier config.py pour refléter vos paramètres d’accès.

Les étapes pour contribuer au projet :
Convention de nommage des commits :

feat: ajout de fonctionnalité

fix: correction de bug

docs: mise à jour de documentation

style: modifications sans impact sur le code (indentation, mise en forme)

refactor: refonte de code sans ajout de fonctionnalité

perf: amélioration des performances

test: ajout ou correction de tests

Exemple de commit :

feat: ajout de la fonctionnalité de location de jeux

main : stable, version de production

dev : branche de développement principale

feature/<nom> : pour les nouvelles fonctionnalités

Étapes de contribution :

Forker le projet

Créer une branche dédiée

Proposer une Pull Request vers dev

Attendre la revue de code d’un autre membre

Brève description des différentes parties du site et des fonctionnalités :

Accueil : Présentation du site et accès rapide aux dernières nouveautés.

Catalogue : Liste des jeux de société avec recherche et filtres par thème, éditeur, popularité.

Fiche jeu : Détails, avis des utilisateurs, possibilité de commenter ou noter.

Événements : Annonces de tournois, rencontres ou conventions locales.

Location de jeux : Plateforme d’échange et location entre membres.

Espace utilisateur : Gestion du profil, contributions.

Pull Requests : historique des révisions de code et des contributions de chaque membre
Toutes les contributions sont visibles dans l’historique du dépôt Git.
