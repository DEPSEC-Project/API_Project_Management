from app.extensions import db
from app import create_app

#app = create_app()

cheh = """with app.app_context():
    try:
        db.session.execute("SELECT 1")  # Exécute une requête simple
        print("Connexion réussie à la base de données !")
    except Exception as e:
        print(f"Erreur de connexion : ")"""
