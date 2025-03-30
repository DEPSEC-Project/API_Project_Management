from app import create_app # import de la fonction create_app du fichier app/__init__.py

app = create_app()

if __name__ == "__main__": #lancement de l'app 
    app.run(host="0.0.0.0", port=5000, debug=True)
    # app.run(debug=app.config.get("DEBUG"))
