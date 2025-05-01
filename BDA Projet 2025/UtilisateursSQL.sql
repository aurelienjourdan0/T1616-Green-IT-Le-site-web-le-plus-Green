	CREATE DATABASE IF NOT EXISTS details;

	USE details;

	CREATE TABLE utilisateurs (
		id SERIAL PRIMARY KEY,
		username VARCHAR(150) UNIQUE NOT NULL,
		email VARCHAR(255) UNIQUE NOT NULL,
		password_hash TEXT NOT NULL,
		date_inscription TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	);

	-- Affiche toutes les tables
	SHOW TABLES;

	-- Affiche le contenu de la table 'jeu'
	SELECT * FROM jeu;
	SELECT * FROM ratings;
	SELECT * FROM utilisateurs;