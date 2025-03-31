from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

#from depsec_models.database import db

db = SQLAlchemy
jwt = JWTManager()
