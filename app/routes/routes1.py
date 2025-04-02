import requests
from flask import Blueprint, current_app, json, request, jsonify
from flask_jwt_extended import create_access_token
from app.extensions import db
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import re
from app.services.auth import verify_token
from app.extensions import db
from depsec_db.models import Project, User
#from depsec_models.models import * #import des modèles depuis le package


projets_bp = Blueprint("projets", __name__)
limiter = Limiter(get_remote_address, default_limits=["5 per minute"])


# ------------------------------------------------------------------------------------------------------------ #

def return_all_proj():
   return Project.query.all()


def return_project(proj):
   for p in return_all_proj():
       if proj in p.values():
           return p

def return_project_by_id(id):
    return Project.query.get(id)

def add_dico(dico):
    projects = return_all_proj()
    if projects != []:
        for d in projects:
            if d.titre == dico["titre"]:
                return jsonify({"error": f"Le nom de projet {d.titre} existe deja !"}), 400
        
    # trouve le + grand id
    max_id = max([p.id for p in projects]) if projects else 0
    
    dico['id'] = max_id + 1

    new_project = Project(
        id = dico['id'],
        auteur_id=dico["auteur_id"],
        titre=dico["titre"],
        status=dico["status"],
        path=dico["path"]
    )

    db.session.add(new_project)
    db.session.commit()

    ### requête avec la table SBOM pour créer un SBOM ###
    requests.post("http://jeanclaudenunes.online:5010/", headers=jsonify(new_project.to_dict()))
    return jsonify({"message": f"Projet {new_project.titre} ajoute avec succes"}), 200

def del_dico(id):
    project = return_project_by_id(id)

    if not project:
        return jsonify({"error": f"Projet avec l'ID {id} non trouve"}), 404

    db.session.delete(project)
    db.session.commit()

    return jsonify({"message": f"Projet avec l'ID {id} supprime avec succes"}), 200

# ------------------------------------------------------------------------------------------------------------ #


@projets_bp.route('/', methods=['GET'])
def get_projects():
    if verify_token() == False and current_app.config["FLASK_ENV"] !="development" : #verifier que le token est valide ( a mettre dans chaque route) et qu'on est pas en environnement de dev
        return jsonify({"msg": "Token invalide / Utilisateur non autorise"}), 401
    
    return jsonify([project.to_dict() for project in Project.query.all()])

@projets_bp.route('/<int:project_id>', methods=['GET'])
def get_project_by_id(project_id):
    project = Project.query.get(project_id)
    if not project:
        return jsonify({'error': 'Projet non trouvé'}), 404
    return jsonify(project.to_dict()), 200

@projets_bp.route('/', methods=['POST'])
def add_project():
    if verify_token() == False and current_app.config["FLASK_ENV"] != "development":
        return jsonify({"msg": "Token invalide / Utilisateur non autorise"}), 401

    data = request.get_json()

    if not data:
        return jsonify({"error": "Le format de vos donnees n'est pas bon !!"}), 400

    required_fields = ["titre", "auteur_id", "status", "path"]
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Parametres manquants'}), 400

    titre = data["titre"]
    auteur_id = data["auteur_id"]
    status = data["status"]
    path = data["path"]

    # vérifie que l'utilisateur existe dans la table User
    user = User.query.get(auteur_id)
    if not user:
        return jsonify({"error": "L'utilisateur spécifié n'existe pas"}), 404

    if isinstance(auteur_id, int) and status in ["Accept", "Refuse"]:
        project_data = {
            "auteur_id": auteur_id,
            "titre": titre,
            "status": status,
            "path": path
        }
        return add_dico(project_data)
    else:
        return jsonify({'error': 'Parametres aux mauvais formats !'}), 400
       

@projets_bp.route("/<id>", methods=["DELETE"])
def del_project(id):
    return del_dico(id)