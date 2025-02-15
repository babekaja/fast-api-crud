# CRUD Utilisateurs avec FastAPI, MySQL et HTML/CSS

Ce projet est une application CRUD (Create, Read, Update, Delete) permettant la gestion des utilisateurs via une API REST développée avec FastAPI, une base de données MySQL et une interface en HTML/CSS.

## Fonctionnalités
- Ajouter un utilisateur
- Lire la liste des utilisateurs
- Mettre à jour un utilisateur
- Supprimer un utilisateur
- Interface web simple pour interagir avec l'API

---

## Prérequis
Avant de commencer, assure-toi d'avoir installé :
- [Python 3.10+](https://www.python.org/downloads/)
- [MySQL (WAMP, XAMPP ou MySQL Server)](https://dev.mysql.com/downloads/)
- [Git](https://git-scm.com/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

---

## Installation

### 1. Cloner le projet
```sh
git clone [https://github.com/babekaja/nom-du-repo.git](https://github.com/babekaja/CRUD-avec-FASTAPI.git)
cd nom-du-repo
```

### 2. Créer un environnement virtuel et installer les dépendances
```sh
python -m venv .venv
source .venv/bin/activate  # Sur Linux/macOS
.venv\Scripts\activate    # Sur Windows
pip install -r requirements.txt
```

### 3. Configurer la base de données MySQL

Assure-toi que MySQL est en cours d'exécution et crée une base de données :
```sql
CREATE DATABASE fastapi_users;
```

### 4. Lancer le serveur
```sh
uvicorn main:app --reload
```
L'API sera accessible sur : [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Structure du Projet
```
nom-du-repo/
│── app/
│   ├── main.py          # Point d'entrée FastAPI
│   ├── models.py        # Modèles SQLAlchemy
│   ├── database.py      # Connexion à MySQL
│   ├── schemas.py       # Schémas Pydantic
│   ├── crud.py          # Fonctions CRUD
│   ├── routes.py        # Routes API
│   ├── templates/       # Fichiers HTML
│   ├── static/          # Fichiers CSS/JS
│── README.md            # Documentation
```

---

## Endpoints API

### 1. Ajouter un utilisateur
```http
POST /users/
```
#### Exemple de requête JSON
```json
{
    "name": "John Doe",
    "email": "johndoe@example.com"
}
```

### 2. Lire tous les utilisateurs
```http
GET /users/
```

### 3. Lire un utilisateur par ID
```http
GET /users/{user_id}
```

### 4. Mettre à jour un utilisateur
```http
PUT /users/{user_id}
```
#### Exemple de requête JSON
```json
{
    "name": "John Updated",
    "email": "johnupdated@example.com"
}
```

### 5. Supprimer un utilisateur
```http
DELETE /users/{user_id}
```

---

## Interface Web
Une interface utilisateur simple en HTML/CSS permet d'interagir avec l'API.
Lance le projet et ouvre [http://127.0.0.1:8000](http://127.0.0.1:8000) dans ton navigateur.

---

## Contributions
Les contributions sont les bienvenues ! Forke ce projet et soumets une pull request. 😊

---

