import requests
from bs4 import BeautifulSoup
import json
import random


database = []
for i in range(1, 3):
    URL = "https://www.bu.edu/academics/cgs/courses/" + str(i)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'lxml')

    for a in soup.find_all('li'):
        hub_units = []
        if a.span is not None and a.a is not None:
            if a.div is not None:
                for j in a.div.ul.find_all('li'):
                    hub_units.append(j.text)

            if a.a.strong.text != 'New':
                ind_col = a.a.strong.text.index(':')
                course_number = a.a.strong.text[:ind_col]
                course_title = a.a.strong.text[ind_col+2:]
                database.append([course_number, course_title, hub_units])
    print(i)

new_JsonFile = []

for j in database:
    if len(j[2]) != 0:
        object = {}
        object['number'] = j[0]
        object['title'] = j[1]
        object['units'] = j[2]
        new_JsonFile.append(object)


json_Object = json.dumps(new_JsonFile, indent=4)

with open('catalog_sorted_cgs.json', 'w') as f:
    f.write(json_Object)
