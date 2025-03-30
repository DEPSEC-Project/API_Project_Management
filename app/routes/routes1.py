from flask import Blueprint, json, request, jsonify
from flask_jwt_extended import create_access_token
#from app.extensions import db
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import re
from app.services.auth import verify_token
from flask import current_app
#from depsec_models.models import * #import des modèles depuis le package


projets_bp = Blueprint("projets", __name__)
limiter = Limiter(get_remote_address, default_limits=["5 per minute"])


# ---------- Phase de test avant la BDD (comme si test.json était ce qu'on récupérait de la BDD) ------------- #


projects = [
   {
       "id":1,
       "titre":"Gestion des projets",
       "auteur":"Solayman",
       "status":"Accept",
       "SBOM":"Recup"
   },
   {
       "id":2,
       "titre":"Gestion de BDD",
       "auteur":"Pierrot la pinto de la mañana",
       "status":"Refuse",
       "SBOM":"Waiting"
   }
]


def return_all_proj():
   return projects


def return_project(proj):
   for p in projects:
       if proj in p.values():
           return p
      


def add_dico(dico):

    for d in projects:
        if d["titre"] == dico["titre"]:
            return jsonify({"error": f"Le nom de projet {d['titre']} existe deja !"}), 400
        
    # trouve le + grand id
    max_id = max([elem['id'] for elem in projects]) if projects else 0
    
    dico['id'] = max_id + 1
    projects.append(dico)
    
    return return_all_proj()
    #save_json(file_path, data)
    #return jsonify(load_json(file_path)), 200

# ------------------------------------------------------------------------------------------------------------ #


@projets_bp.route('/', methods=['GET'])
def get_projects():
   if verify_token() == False and current_app.config["FLASK_ENV"] !="development" : #verifier que le token est valide ( a mettre dans chaque route) et qu'on est pas en environnement de dev
       return jsonify({"msg": "Token invalide / Utilisateur non autorisé"}), 401


   #data = request.get_json()


   return return_all_proj(), 200
   #return jsonify({"Projects":data.get('titre')}), 200


@projets_bp.route('/', methods=['POST'])
def add_project():
   if verify_token() == False and current_app.config["FLASK_ENV"] !="development" : #verifier que le token est valide ( a mettre dans chaque route) et qu'on est pas en environnement de dev
       return jsonify({"msg": "Token invalide / Utilisateur non autorisé"}), 401


   data = request.get_json()
   
   if not data :
        return jsonify({"error": "Le fomat de vos donnees n'est pas bon !!"}), 400
   
   if data.get("titre") and data.get("auteur") and data.get("status") and data.get("SBOM"):
        titre = data.get("titre")
        auteur = data.get("auteur")
        status = data.get("status")
        sbom = data.get("SBOM")

        if isinstance(auteur, str) and status in ["Accept","Refuse"] and sbom in ["Recup","Waiting"]:
            format = {
                "id":0,
                "titre":titre,
                "auteur":auteur,
                "status":status,
                "SBOM":sbom
            }
            return add_dico(format)
        else :
            return jsonify({'error': 'Parametres aux mauvais formats !'}), 400
   else :
        return jsonify({'error': 'Parametres manquants'}), 400
       
        


@projets_bp.route('/projets', methods=['POST'])
@limiter.limit("5 per minute") #exemple pour limiter le nombre de requetes
def tutu():
   if verify_token() == False and current_app.config["FLASK_ENV"] !="development" : #verifier que le token est valide ( a mettre dans chaque route) et qu'on est pas en environnement de dev
       return jsonify({"msg": "Token invalide / Utilisateur non autorisé"}), 401


   data = request.json


   return jsonify({"msg": "blabla"}), 401