import requests
from bs4 import BeautifulSoup
import json
import random

CATALOG_PATH = 'catalog_final.json'


catalog_descriptions = json.load(open(CATALOG_PATH))

for i, j in enumerate(catalog_descriptions):
    if len(j) == 3:
        catalog_descriptions[i]["prerequisites"] = []

jsonObject = json.dumps(catalog_descriptions, indent=4)

with open('catalog_final_2.json', 'w') as f:
    f.write(jsonObject)
