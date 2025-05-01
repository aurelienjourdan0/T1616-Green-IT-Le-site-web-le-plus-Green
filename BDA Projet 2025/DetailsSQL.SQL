CREATE DATABASE IF NOT EXISTS details;

USE details;

CREATE TABLE IF NOT EXISTS jeu (
    num INT AUTO_INCREMENT PRIMARY KEY,
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    yearpublished INT,
    minplayers INT,
    maxplayers INT,
    playingtime INT,
    minplaytime INT,
    maxplaytime INT,
    minage INT,
    boardgamecategory VARCHAR(255),
    boardgamemechanic VARCHAR(255),
    boardgamefamily VARCHAR(255),
    boardgameexpansion VARCHAR(255),
    boardgameimplementation VARCHAR(255),
    boardgamedesigner VARCHAR(255),
    boardgameartist VARCHAR(255),
    boardgamepublisher VARCHAR(255),
    owned INT DEFAULT 0,
    trading INT DEFAULT 0,
    wanting INT DEFAULT 0,
    wishing INT DEFAULT 0
);

INSERT INTO jeu (id, name, description, yearpublished, minplayers, maxplayers, playingtime, minplaytime, maxplaytime, minage, boardgamecategory, boardgamemechanic, boardgamefamily, boardgameexpansion, boardgameimplementation, boardgamedesigner, boardgameartist, boardgamepublisher, owned, trading, wanting, wishing)
VALUES
(1, 'Catan', 'Un jeu de stratégie où les joueurs colonisent une île.', 1995, 3, 4, 60, 30, 90, 10, 'Stratégie', 'Échange, Placement', 'Famille', NULL, NULL, 'Klaus Teuber', 'Michael Menzel', 'Kosmos', 0, 0, 0, 0),
(2, 'Terraforming Mars', 'Colonisez Mars en terraformant sa surface pour y vivre.', 2016, 1, 5, 120, 90, 150, 12, 'Sci-Fi', 'Gestion de ressources, Draft', 'Expert', NULL, NULL, 'Jacob Fryxelius', 'Isaac Fryxelius', 'FryxGames', 0, 0, 0, 0),
(3, 'Carcassonne', 'Un jeu de tuiles où les joueurs construisent des paysages médiévaux.', 2000, 2, 5, 35, 20, 60, 7, 'Stratégie', 'Placement de tuiles', 'Famille', NULL, NULL, 'Klaus-Jürgen Wrede', 'Clemens Franz', 'Hans im Glück', 0, 0, 0, 0),
(4, 'Gloomhaven', 'Un jeu de société de type donjon-crawler avec des éléments de RPG.', 2017, 1, 4, 120, 60, 180, 14, 'Fantasy', 'Aventure, Scénario', 'Campagne', NULL, NULL, 'Isaac Childres', 'Alexandr Elichev', 'Cephalofair Games', 0, 0, 0, 0),
(5, '7 Wonders', 'Un jeu de civilisation où les joueurs construisent des merveilles.', 2010, 3, 7, 30, 20, 60, 10, 'Civilisation', 'Draft, Collection', 'Famille', NULL, NULL, 'Antoine Bauza', 'Miguel Coimbra', 'Repos Production', 0, 0, 0, 0),
(6, 'Dominion', 'Un jeu de cartes où les joueurs construisent leur deck et cherchent à dominer.', 2008, 2, 4, 30, 20, 45, 13, 'Stratégie', 'Deck-building', 'Famille', NULL, NULL, 'Donald X. Vaccarino', 'Jesse McGrew', 'Rio Grande Games', 0, 0, 0, 0),
(7, 'Azul', 'Un jeu de stratégie où les joueurs placent des tuiles pour marquer des points.', 2017, 2, 4, 30, 20, 45, 8, 'Abstrait', 'Placement de tuiles', 'Famille', NULL, NULL, 'Michael Kiesling', 'Chris Quilliams', 'Plan B Games', 0, 0, 0, 0),
(8, 'Scythe', 'Un jeu de stratégie dans un univers dieselpunk alternatif.', 2016, 1, 5, 115, 90, 140, 14, 'Stratégie', 'Contrôle de territoire, Gestion', 'Expert', NULL, NULL, 'Jamey Stegmaier', 'Jakub Rozalski', 'Stonemaier Games', 0, 0, 0, 0),
(9, 'Wingspan', 'Un jeu de collection d’oiseaux avec des mécaniques de moteur de production.', 2019, 1, 5, 40, 30, 70, 10, 'Nature', 'Collection, Gestion de main', 'Famille', NULL, NULL, 'Elizabeth Hargrave', 'Natalia Rojas', 'Stonemaier Games', 0, 0, 0, 0),
(10, 'Ticket to Ride', 'Un jeu où les joueurs construisent des chemins de fer à travers l\'Amérique.', 2004, 2, 5, 60, 30, 90, 8, 'Stratégie', 'Collection de cartes', 'Famille', NULL, NULL, 'Alan R. Moon', 'Julian K. Richards', 'Days of Wonder', 0, 0, 0, 0),
(11, 'Pandemic', 'Un jeu coopératif où les joueurs luttent contre des épidémies mondiales.', 2008, 2, 4, 45, 30, 60, 8, 'Coopératif', 'Gestion de ressources', 'Famille', NULL, NULL, 'Matt Leacock', 'Chris Quilliams', 'Z-Man Games', 0, 0, 0, 0),
(12, 'Brass: Birmingham', 'Un jeu économique sur la révolution industrielle anglaise.', 2018, 2, 4, 120, 90, 150, 14, 'Économique', 'Connexion de réseaux', 'Expert', NULL, NULL, 'Gavan Brown', 'Ian O\'Toole', 'Roxley Games', 0, 0, 0, 0),
(13, 'Root', 'Un jeu asymétrique de guerre et d’aventure dans une forêt animée.', 2018, 2, 4, 90, 60, 120, 10, 'Stratégie', 'Asymétrique', 'Fantasy', NULL, NULL, 'Cole Wehrle', 'Kyle Ferrin', 'Leder Games', 0, 0, 0, 0),
(14, 'The Crew', 'Un jeu de plis coopératif dans l’espace.', 2019, 2, 5, 20, 15, 30, 10, 'Coopératif', 'Plis', 'Famille', NULL, NULL, 'Thomas Sing', 'Marco Armbruster', 'Kosmos', 0, 0, 0, 0),
(15, 'Splendor', 'Un jeu de stratégie où les joueurs collectent des gemmes pour acheter des cartes.', 2014, 2, 4, 30, 20, 45, 10, 'Stratégie', 'Collection de ressources', 'Famille', NULL, NULL, 'Marc André', 'Pascal Quidault', 'Space Cowboys', 0, 0, 0, 0),
(16, 'Codenames', 'Un jeu d’associations de mots où les équipes s’affrontent.', 2015, 2, 8, 15, 10, 30, 14, 'Famille', 'Déduction', 'Ambiance', NULL, NULL, 'Vlaada Chvátil', 'Tomáš Kučerovský', 'Czech Games Edition', 0, 0, 0, 0),
(17, 'Betrayal at House on the Hill', 'Un jeu semi-coopératif d’exploration de maison hantée.', 2004, 3, 6, 60, 45, 90, 12, 'Horreur', 'Exploration, Trahison', 'Narratif', NULL, NULL, 'Bruce Glassco', 'N/A', 'Avalon Hill', 0, 0, 0, 0),
(18, 'Love Letter', 'Un jeu de cartes où les joueurs essaient d\'envoyer des lettres d\'amour.', 2012, 2, 4, 20, 15, 30, 8, 'Cartes', 'Déduction', 'Famille', NULL, NULL, 'Seiji Kanai', 'N/A', 'Z-Man Games', 0, 0, 0, 0),
(19, 'King of Tokyo', 'Un jeu où des monstres s’affrontent pour le contrôle de Tokyo.', 2011, 2, 6, 30, 20, 45, 8, 'Action', 'Jets de dés', 'Famille', NULL, NULL, 'Richard Garfield', 'Regis Torres', 'IELLO', 0, 0, 0, 0),
(20, 'Everdell', 'Construisez une ville prospère dans une forêt peuplée de créatures.', 2018, 1, 4, 90, 60, 120, 13, 'Fantasy', 'Placement d’ouvriers', 'Nature', NULL, NULL, 'James A. Wilson', 'Andrew Bosley', 'Starling Games', 0, 0, 0, 0);

-- Affiche toutes les tables
SHOW TABLES;

-- Affiche le contenu de la table 'jeu'
SELECT * FROM jeu;
SELECT * FROM ratings;
SELECT * FROM utilisateurs;