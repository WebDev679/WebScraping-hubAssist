import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

CATALOG_PATH = 'catalog_cgs.json'

catalog_descriptions = json.load(open(CATALOG_PATH))

database = []
for w in range(1, 3):
    URL = "https://www.bu.edu/academics/cgs/courses/" + str(w)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'lxml')

    for a in soup.find_all('li'):
        if a.a is not None:
            hoursPerWeek = [] 
            URL_new = "https://www.bu.edu/" + a.a['href']
            page_new = requests.get(URL_new)
            soup_new = BeautifulSoup(page_new.content, 'lxml')
            i = soup_new.find_all('div', {'class': 'cf-course'})
            if len(i) != 0:
                i = i[0] 
            else:
                continue
            if a.a.strong.text != 'New':
                ind_col = a.a.strong.text.index(':')
                print(a.a.strong.text[:ind_col])
            for j in i.find_all('table'):
                for k, l in enumerate(j.find_all('td')):
                    if k ==3:
                        if l.text == "ARR TBD-TBD" or l.text == "TBD-TBD":
                            continue
                        components = l.text.split(' ')
                        days = len(components[0])
                        text = l.text
                        text = text.split()
                        if text[1][1] == ":":
                            text[1] = "0" + text[1]
                        if text[2][0] == "p" and text[1][0:2] != "12":
                            text[1] = str(int(text[1][:2]) + 12) + text[1][2:]
                        text[2] = text[2][3:]
                        if text[2][1] == ":":
                            text[2] = "0" + text[2]
                        if text[3][0] == "p" and text[2][0:2] != "12":
                            text[2] = str(int(text[2][:2]) + 12) + text[2][2:]
                        t1 = datetime.strptime(text[1] + ":00", "%H:%M:%S")
                        t2 = datetime.strptime(text[2] + ":00", "%H:%M:%S")
                        delta = t2 - t1
                        hours = delta.total_seconds()/3600
                        hoursPerWeek.append(hours*days)

                    
            if a.a.strong.text != 'New':
                ind_col = a.a.strong.text.index(':')
                course_number = a.a.strong.text[:ind_col]
                if len(hoursPerWeek) > 0:
                    hoursPerWeek = max(hoursPerWeek)
                else:
                    hoursPerWeek = 0
                database.append([course_number, hoursPerWeek])
                print(database[-1])
        print(w)

print(database)

newJsonFile = []

for i in catalog_descriptions:
    for j in database:
        if i['number'] in j[0]:
            i['hoursPerWeek'] = j[1]
            break
    newJsonFile.append(i)

jsonObject = json.dumps(newJsonFile, indent=4)

with open('catalog_cgs_new.json', 'w') as f:
    f.write(jsonObject)