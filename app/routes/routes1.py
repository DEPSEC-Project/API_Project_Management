from flask import Blueprint, request, jsonify
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

@test_bp.route('/toto', methods=['GET'])
def toto():
    if verify_token() == False and current_app.config["FLASK_ENV"] !="development" : #verifier que le token est valide ( a mettre dans chaque route) et qu'on est pas en environnement de dev
        return jsonify({"msg": "Token invalide / Utilisateur non autorisé"}), 401

    data = request.json
    return jsonify({"msg":"blabla cool"}), 200

@test_bp.route('/tutu', methods=['POST'])
@limiter.limit("5 per minute") #exemple pouur limiter le nombre de requetes
def tutu():
    if verify_token() == False and current_app.config["FLASK_ENV"] !="development" : #verifier que le token est valide ( a mettre dans chaque route) et qu'on est pas en environnement de dev
        return jsonify({"msg": "Token invalide / Utilisateur non autorisé"}), 401

    data = request.json

    return jsonify({"msg": "blabla"}), 401




