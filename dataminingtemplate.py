# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

session = requests.session()
for x in range(1,3883):

    exec("req = session.get('http://joewoodsworks.com/%s')" % (x))
    doc = BeautifulSoup(req.content, 'html.parser')
    arrayness = doc.find_all("div",{"class":"cc-publishtime"})
    if arrayness:
        print arrayness[0]