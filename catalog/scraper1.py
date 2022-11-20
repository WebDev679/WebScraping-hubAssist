import requests
from bs4 import BeautifulSoup
import json
import random


database = []
URL = "https://www.bu.edu/academics/cas/courses/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'lxml')

for a in soup.find_all('li'):
    professors = []
    print(a)
    if a.span is not None and a.a is not None:
        URL_new = a.a['href']
        URL_new = "https://www.bu.edu" + URL_new
        print(URL_new)
        page1 = requests.get(URL_new)
        soup1 = BeautifulSoup(page1.content, 'lxml')
        i = soup1.find_all('div', {'class': 'cf-course'})
        for j in i:
            for k in j.find_all('table'):
                for l, h in enumerate(k.find_all('td')):
                    if l ==1:
                        professors.append(h.text)

        professors = [*set(professors)]
        print(professors)


"""for a in soup.find_all('li'):
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
    f.write(json_Object)"""
