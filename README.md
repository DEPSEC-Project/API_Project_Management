# Project Management API

###### Ce micro-service va nous permettre de gérer tous les autres micro-services en les ajoutant, supprimant, avec un système de validation /refus et en se basant sur le système d'authentification.

## Arborescense
Voici l'arborescence de notre API, avec en commentaire pour chaque dossier/fichier : 

```
project_management_API/
├── app/
│   ├── config.py         # Configuration de l'application ( mode dev, staging, prod, ...)
│   ├── __init__.py       # Initialisation de l'application Flask (création de l'app )
│   ├── extensions.py      # Gestion des bibliothèques (SQLALchemy, JWT,flask migrate,...)
│   ├── routes/           # Dossier pour les routes (blueprints)
│   │   ├── auth.py       # Routes d'authentification (inscription, connexion, JWT)
│   │   ├── courses.py  # Routes pour la gestion des routes liées à un autre sujet
│   ├── services/           # Dossier pour le code python avec vos fonctions etc
│   │   ├── get_projects.py       # fonctions liées à la récupération des projets
│   │   ├── add_project.py       # fonctions liées à l'ajout d'un projet
│   │   ├── del_project.py       # fonctions liées à le suppression d'un projet
│   ├── data/           # Dossier pour le code python avec vos fonctions etc
│   │   ├── data.yaml       # Contrat d'interface
├── requirements.txt      # Dépendances Python
├── .env                  # Fichier pour les variables d'environnement
├── app.py                # Point d'entrée de l'application
├── Dockerfile            # Fichier de l'image docker du microservice
└── README.md             # Documentation de l'API
```

## Lists

### Unordered

* Item 1
* Item 2
* Item 2a
* Item 2b
    * Item 3a
    * Item 3b

### Ordered

1. Item 1
2. Item 2
3. Item 3
    1. Item 3a
    2. Item 3b

## Images

![This is an alt text.](/image/sample.webp "This is a sample image.")

## Links

You may be using [Markdown Live Preview](https://markdownlivepreview.com/).

## Blockquotes

> Markdown is a lightweight markup language with plain-text-formatting syntax, created in 2004 by John Gruber with Aaron Swartz.
>
>> Markdown is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor.

## Tables

| Left columns  | Right columns |
| ------------- |:-------------:|
| left foo      | right foo     |
| left bar      | right bar     |
| left baz      | right baz     |

## Blocks of code

```
let message = 'Hello world';
alert(message);
```

## Inline code

This web site is using `markedjs/marked`.

