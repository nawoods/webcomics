# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

session = requests.session()

#exec("req = session.get('http://joewoodsworks.com/%s')" % (x))
req = session.get('https://en.wikipedia.org/wiki/List_of_webcomics')
doc = BeautifulSoup(req.content, 'html.parser')
firstlevel = doc.findAll("li")
for boop in firstlevel:
    secondlevel = boop.findAll("i")
    if secondlevel:
        for beep in secondlevel:
            thirdlevel = beep.findAll("a")
            if thirdlevel:
                #print thirdlevel
                for baap in thirdlevel:
                    print [baap['href'], baap['title']]
