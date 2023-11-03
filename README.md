# initialisation

```sh
python3 -m venv venv
source venv/bin/activate

./venv/bin/pip install django
# .\venv\Scripts\pip install django (win10)

```

# démarrage du projet

```sh
django-admin startproject config .

```

# Créer admin / Table

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

# ajouter l'app

```sh
django-admin startapp www

```

# Test de fontionnement de l'app

```sh
python manage.py runserver

```

# Si modification DB

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# Article

title
content
published_at
user
status
category 1-N
tags N-N

icon PJ
cover

```sh
./venv/bin/pip install Pillow #pour exploiter les images par python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


```

# importer des datas

- Utiliser sqlite3 en direct = si schema simple
- Se greffer sur Djando dans un script à part

```sh
./venv/bin/pip install django-extensions

#sert à faire des schemas (marche pas)
# ./venv/bin/pip install pydotplus
# ./venv/bin/python manage.py graph_models -a -o models.png
```

- créer un fichier import.py
  - importer nos models Articles, Categories, tags
  - charger les données de l'api
  - pour chaque :
    - instancier un Article, affecter les valeurs, save
    - charger les images, attacher aux articles
    - tags

```sh
# installer requests
pip install requests

- python manage.py runscript import.py

```

# Rendu routage url / template

- templates/
  - base.html
- www/templates/
  - list.html
  - single.html
  - cat.html
  - tags.html

## Liens "category" et "tags"

- models -> views/templates -> urls
