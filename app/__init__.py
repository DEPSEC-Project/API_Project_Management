from flask import Flask, jsonify
from app.config import *
from app.extensions import jwt
import os
from dotenv import load_dotenv


__version__ = "1.0.1" # géré automatiquement par la CI


load_dotenv(".env")
def create_app():
   app = Flask(__name__)


   app.config.from_object(config[os.getenv("FLASK_ENV") or "development"])#en mode dev par défaut si rien de spécifié


   #db.init_app(app)
   jwt.init_app(app)


   @jwt.unauthorized_loader   # gérer le cas ou le client n'est pas authentifié
   def unauthorized_callback(callback):
       return jsonify({"msg": "Token invalide ou manquant. veuillez vous authentifier."}), 401


   from app.routes.routes1 import projets_bp


   app.register_blueprint(projets_bp, url_prefix='/projets')


   return app