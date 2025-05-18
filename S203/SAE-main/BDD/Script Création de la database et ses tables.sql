DROP DATABASE IF EXISTS Admin_serveur;

CREATE DATABASE Admin_serveur;

USE Admin_serveur;

CREATE TABLE Type_serveur(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    type_serveur VARCHAR(40),
    descript VARCHAR(300)
);

CREATE TABLE Serveurs(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(40),
    nombre_processeur INT UNSIGNED,
    memoire INT UNSIGNED,
    stockage INT UNSIGNED,
    id_type INT UNSIGNED,
    CONSTRAINT fk_type_serveur
		FOREIGN KEY (id_type)
        REFERENCES Type_serveur(id)
);

CREATE TABLE Utilisateur(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(30),
    prenom VARCHAR(30),
	mail VARCHAR(100)
);

CREATE TABLE Services_disponible(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(40),
    memoire_necessaire INT NOT NULL
);

CREATE TABLE Services_en_cours(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    id_service INT UNSIGNED,
    id_serveur INT UNSIGNED,
	date_lancement DATE,
    memoire_utiliser INT,
	CONSTRAINT fk_service
		FOREIGN KEY (id_service)
        REFERENCES Services_disponible(id),
    CONSTRAINT fk_serveur
		FOREIGN KEY (id_serveur)
        REFERENCES Serveurs(id)
);

CREATE TABLE Application_disponible(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(40),
    logo VARCHAR(100)
);

CREATE TABLE Application_en_cours(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    id_app INT UNSIGNED,
    id_serveur INT UNSIGNED,
    id_utilisateur INT UNSIGNED,
    CONSTRAINT fk_app
		FOREIGN KEY (id_app)
        REFERENCES Application_disponible(id),
    CONSTRAINT fk_serveur_utiliser
		FOREIGN KEY (id_serveur)
        REFERENCES Serveurs(id),
    CONSTRAINT fk_utilisateur
		FOREIGN KEY (id_utilisateur)
        REFERENCES Utilisateur(id)
);