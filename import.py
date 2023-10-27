from www.models import Articles, Categories, Tags
from datetime import datetime
import json
from django.core.files import File
import requests
from io import BytesIO

# Chargement des données
URL = "https://api.atontour.org/v1/games/"

response = requests.get(URL)
response_json = response.json()
print(response_json)
