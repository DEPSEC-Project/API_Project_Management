from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from depsec_db.extensions import db

db = db

#from depsec_models.database import db

jwt = JWTManager()