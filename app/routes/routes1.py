from flask import Blueprint, json, request, jsonify
from flask_jwt_extended import create_access_token
#from app.extensions import db
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import re
from app.services.auth import verify_token
from flask import current_app
#from depsec_models.models import * #import des modèles depuis le package

test_bp = Blueprint("test", __name__)
limiter = Limiter(get_remote_address, default_limits=["5 per minute"])

# ---------- Phase de test avant la BDD (comme si test.json était ce qu'on récupérait de la BDD) ------------- #

with open('test.json', 'r') as project:
    projects = json.load(project)

def return_project(proj):
    for p in projects:
        if proj in p.values():
            return p
        
def is_project(title):
    for p in projects:
        if title in p.values():
            return True

# ------------------------------------------------------------------------------------------------------------ #

@test_bp.route('/projets', methods=['GET'])
def get_projects():
    if verify_token() == False and current_app.config["FLASK_ENV"] !="development" : #verifier que le token est valide ( a mettre dans chaque route) et qu'on est pas en environnement de dev
        return jsonify({"msg": "Token invalide / Utilisateur non autorisé"}), 401

    data = request.json
    if request.method == 'GET':
        return jsonify({"Projects":data}), 200

@test_bp.route('/projets', methods=['POST'])
def add_project():
    if verify_token() == False and current_app.config["FLASK_ENV"] !="development" : #verifier que le token est valide ( a mettre dans chaque route) et qu'on est pas en environnement de dev
        return jsonify({"msg": "Token invalide / Utilisateur non autorisé"}), 401

    data = request.json

    try :
        id = data["id"]
        titre = data["titre"]
        auteur = data["auteur"]
        status = data["status"]
        sbom = data["SBOM"]

        format = {
            "id":id,
            "titre":titre,
            "auteur":auteur,
            "status":status,
            "SBOM":sbom
        }

        if request.method == 'POST':
            if is_project(titre) != True and isinstance(id, int) and isinstance(auteur, str) and status in ["Accept","Refuse"] and sbom in ["Recup","Waiting"]:
                return jsonify(format), 200
        
    except:
        return jsonify({"Format de votre requête invalide": "Format de vos valeurs invalide"}), 203

@test_bp.route('/projets', methods=['POST'])
@limiter.limit("5 per minute") #exemple pour limiter le nombre de requetes
def tutu():
    if verify_token() == False and current_app.config["FLASK_ENV"] !="development" : #verifier que le token est valide ( a mettre dans chaque route) et qu'on est pas en environnement de dev
        return jsonify({"msg": "Token invalide / Utilisateur non autorisé"}), 401

    data = request.json

    return jsonify({"msg": "blabla"}), 401