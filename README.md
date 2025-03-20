# DEPSEC-TemplateAPI

Template d'API flask qui correspond à l'architecture d'APIs définie pour l'ensemble du projet DEPSEC, elle sert à simplifier la création d'une nouvelle API ainsi qu'à uniformiser nos APIs.

## Fonctionnalités implémentées par cette template
La template gère déjà l'exécution d'une API, il est déjà possible de l'éxécuter ici, on a un seul blueprint test_bp (app/routes/routes1:11) dans lequel on a deux routes :
- /test/toto qui gère les requêtes GET

- /test/tutu qui gère les requêtes POST

Le template permet d'avoir déjà une liste de dépendances établie pour le projet, à laquelle il suffira d'ajouter les nouvelles dépendances.

Il permet la gestion d'environnements de Dev, Test et Prod ( config.py ) en se basant sur des variables d'environnements dont voici une liste :
```bash
FLASK_ENV=development ou testing ou production
JWT_SECRET_KEY=mdpsecretmalade

DEV_DATABASE_URL=postgresql://user:password@db:5432/basededev
TEST_DATABASE_URL=postgresql://user:password@db:5432/basedetest
PROD_DATABASE_URL=postgresql://user:password@db:5432/basedeprod

FLASK_PORT=5000
```
### Intégration continue et tests
Les fichiers worflows servent à automatiquement réaliser des actions notamment lors d'un pull request afin d'améliorer notre productivité, cela va installer les dépendances, lancer l'application puis exécuter tous les tests écrits dans test/*





## Comment s'en servir ? 
Tout d'abord, un dépot template sert de modèle à un nouveau template, dans les faits, un nouveau template copiera l'ensemble du modèle, sans conserver l'historique git du dépot, à l'inverse d'un fork, pour ce faire en premier lieu :
![image](https://github.com/user-attachments/assets/ba4ed3c8-360a-4582-8e36-26ebc39f6748)
<br></br>
Il faut ensuite choisir le nom de votre nouveau repo,  copier les branches de la template puis créer le dépot.
![image](https://github.com/user-attachments/assets/f8d44895-9f8a-40ce-b4fa-72e30ad0b8bf)

Vous aurez ensuite votre nouveau dépot reprenant tout l'ensemble de l'ancien dépot. 

## A modifier
- Fichier README.md avec les informations relatives à votre API
- Fichier DOCKERFILE de configuration de l'image docker
- Fichier app/__ init__.py : gérer les blueprints avec leurs préfixes
  ```python
  from app.routes.fichier.py import <nom_blueprint>
  app.register_blueprint(<nom _blueprint>, url_prefix='/route1')
  app.register_blueprint<nom _blueprint>, url_prefix='/route2')
  ```
- fichiers app/routes/*, définir les endpoints associés aux blueprints ainsi que les méthodes et chemins associés:
  ```python
  <nom_blueprint> = Blueprint("<nom>", __name__) # exemple de nom : users / auth
  @<nom_blueprint>.route('/tutu', methods=['POST'])
  @limiter.limit("5 per minute") #comme on veut
  def <nom_fonction>():
    data = request.json
    #implémentation de la fonction etc
    return jsonify({"msg": ""}), 401
  #autant d'endpoints qu'on veut...
  ```
- Fichier requirements.txt dans le cas où vous utilisez des bibliothèques supplémentaires
- Fichier .env avec les informations qui vont bien c'est à dire le bon URL pour la BDD etc
## Exécution du serveur

1. Démarrer l'application Flask
```python
flask run
```
Par défaut, l'API tourne sur http://127.0.0.1:5000/

2. Exécution en mode debug
```python
FLASK_ENV=development
flask run
```
