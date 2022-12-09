import requests
from bs4 import BeautifulSoup
import json
import random

CATALOG_PATH = 'catalog2.json'

courses_taken = ['CS 111', 'CS 112', 'MA 123']

jsonObject = [
{
    "number": "ENG BE 466",
    "prerequisites": [
      "BE 465",
      "WR 120"
    ],
    "title": "Biomedical Engineering Senior Project",
    "units": [
      "Oral and/or Signed Communication",
      "Digital/Multimedia Expression",
      "Research and Information Literacy",
      "Writing-Intensive Course"
    ]
  }
]

def prereq_reduction(G):
    courses = G
    for t, v in enumerate(courses):
        count = 0
        try:
            print(v['prerequisites'])
            for d in v['prerequisites']:
                for s in courses_taken:
                    print(d)
                    print(s)
                    if d == s:
                        count += 1
            if count != len(v['prerequisites']):
                del courses[t]
        except:
            pass
    return courses

jsonObject = prereq_reduction(jsonObject)
print(jsonObject)
