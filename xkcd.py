# -*- coding: utf-8 -*-

import json

import requests
from bs4 import BeautifulSoup

session = requests.session()
comic_info = []
x = 1

while True:
    x += 1
    
    exec("req = session.get('http://xkcd.com/%s')" % (x))
    doc = BeautifulSoup(req.content, 'lxml')
    
    if doc.title.string == "404 - Not Found": break
    
    # attrs is the list of all attributes within the comic's img tag
    comic_dict = doc.find("div",{"id":"comic"}).img.attrs
    comic_dict['num'] = x
    
    # dates of comics aren't on xkcd's website, mined from a fan wiki
    exec("req2 = session.get('http://www.explainxkcd.com/wiki/index.php/%s')" % (x))
    doc2 = BeautifulSoup(req2.content, 'lxml')
    date = doc2.find("a", "external text")
    
    # trim the comic number off of the string that contains the date
    if date: 
        date = date.string
        j = date.index('(')
        date = date[j+1:-1]
        comic_dict['date'] = date
        
    
    comic_info.append(comic_dict)
    
    
with open("xkcd.txt", "w") as f:
    f.write(json.dumps(comic_info))