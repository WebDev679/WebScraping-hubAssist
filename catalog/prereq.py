import requests
from bs4 import BeautifulSoup
import json
import random

CATALOG_PATH = 'catalog_sorted_qst.json'

catalog_descriptions = json.load(open(CATALOG_PATH))


database = []
for k in range(1, 23):
    URL = "https://www.bu.edu/academics/questrom/courses/" + str(k)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'lxml')


    for a in soup.find_all('li'):
        if a.span is not None and a.a is not None:
            if 'Prereq' in str(a.span):
                prerequistes = []
                prereqString = str(a.span.text).replace(';', '')
                prereqString = prereqString.replace(' ', '')
                for i, s in enumerate(prereqString):
                    if s in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and prereqString[i-1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        appendString = prereqString[i-2:i] + ' ' + prereqString[i:i+3]
                        prerequistes.append(appendString)
                database.append([a.a.strong.text, prerequistes])

    print(k)

newJsonFile = []

for i in catalog_descriptions:
    for j in database:
        if i['number'] in j[0]:
            i['prerequisites'] = j[1]
            break
    newJsonFile.append(i)

jsonObject = json.dumps(newJsonFile, indent=4)

with open('catalog_qst.json', 'w') as f:
    f.write(jsonObject)


"""
            prereqString = prereqString.replace('or equivalent', '')
            prereqString = prereqString.replace('or consent', '')
            if ' or ' in prereqString:
                pos = prereqString.find(' or ')
                if prereqString[pos-3] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    appendString = prereqString[pos-5:pos-3] + ' ' + prereqString[pos-3:pos]
                    prerequistes.append([appendString])
                    prereqString = prereqString.replace(prereqString[pos-6:pos], '')
                if prereqString[pos+7] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    appendString = prereqString[pos+4:pos+6] + ' ' + prereqString[pos+6:pos+10]
                    prerequistes.append([appendString])
                    prereqString = prereqString.replace(prereqString[pos+3:pos+10], '')
                for i, s in enumerate(prereqString):
                    if s in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and prereqString[i-1] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        appendString = prereqString[i-2:i] + ' ' + prereqString[i:i+3]
                        prerequistes.append(appendString)
            if len(prerequistes) == 1:
                prerequistes = prerequistes[0]
            else:

"""
"""for a in soup.find_all('li'):
    if a.span is not None and a.a is not None:
        if 'Prereq' in str(a.span):
            prerequistes = []
            print(a.span.text.split(' or '))
            split_ = [prerequistes.append(str(a.span).split(' or '))]"""
