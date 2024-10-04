import sqlite3
import pandas as pd


# Connexion à une base de données SQLite
conn = sqlite3.connect('brief_6.db')

# Chemin vers la base de données
db_path = 'C:/Users/Utilisateur/PycharmProjects/Brief_6'

# Création d'un curseur pour exécuter des commandes SQL
cursor = conn.cursor()


# Supprimer les tables Clients et Commandes si elles existent déjà
cursor.execute("DROP TABLE IF EXISTS Commandes;")
cursor.execute("DROP TABLE IF EXISTS Clients;")


# Création de la table Clients
cursor.execute('''
CREATE TABLE IF NOT EXISTS "Client" (
	"Client_ID" INTEGER NOT NULL UNIQUE,
	"Nom" VARCHAR NOT NULL,
	"Prénom" VARCHAR NOT NULL,
	"email" VARCHAR NOT NULL UNIQUE,
	"Téléphone" VARCHAR,
	"Date_Naissance" DATE,
	"Adresse" VARCHAR,
	"Consentement_Marketing" BOOLEAN NOT NULL,
	PRIMARY KEY("Client_ID")
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS "Commandes" (
	"Commande_ID" INTEGER NOT NULL UNIQUE,
	"Client_ID" INTEGER NOT NULL,
	"Date_Commande" DATE NOT NULL,
	"Montant_Commande" REAL NOT NULL,
	PRIMARY KEY("Commande_ID"),
	FOREIGN KEY ("Client_ID") REFERENCES "Client"("Client_ID")
	ON UPDATE NO ACTION ON DELETE NO ACTION
)
''')


# Lecture et importation du fichier CSV des clients
try:
    clients_df = pd.read_csv('csv_clients.csv)
    clients_df.to_sql('Client', conn, if_exists='replace', index=False)  # Remplace la table si elle existe
    print("Les données des clients ont été importées avec succès.")
except Exception as e:
    print(f"Erreur lors de l'importation des clients : {e}")


# Lecture et importation du fichier CSV des commandes
try:
    commandes_df = pd.read_csv('csv_commandes.csv')
    commandes_df.to_sql('Commande', conn, if_exists='replace', index=False)  # Remplace la table si elle existe
    print("Les données des commandes ont été importées avec succès.")
except Exception as e:
    print(f"Erreur lors de l'importation des commandes : {e}")


cursor.execute("SELECT * FROM Client WHERE Consentement_Marketing = 1")

# Fermeture de la connexion
conn.close()