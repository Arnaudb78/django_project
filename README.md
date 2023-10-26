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

# ajouter l'app

```sh
django-admin startapp www

```

# Test de fontionnement de l'app

```sh
python manage.py runserver

```
