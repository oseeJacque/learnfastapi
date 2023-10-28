from sqlalchemy import create_engine, MetaData

DB_NAME = 'test1'  # Nom de la base de données SQLite

# Utilisez l'URL de connexion SQLite (utilisez 'sqlite:///NomDeLaBaseDeDonnees.db')
engine = create_engine(f'sqlite:///{DB_NAME}.db')


meta = MetaData() 
conn = engine.connect() 