AUTH_SERVICE_URL = "http://depsecauth:5000/verify"
import requests
from flask import request, jsonify

def verify_token(): #requêter le service d'authentification pour vérifier que le token est bien valdie 
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return False

    token = auth_header.split(" ")[1]
    response = requests.post(AUTH_SERVICE_URL, headers={"Authorization": f"Bearer {token}"})
    
    if response.status_code == 200:
        return True
    return False