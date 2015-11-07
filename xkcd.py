# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

session = requests.session()
for x in range(1,1600):

    exec("req = session.get('http://xkcd.com/%s')" % (x))
    doc = BeautifulSoup(req.content, 'html.parser')
    comic_dict = doc.find("div",{"id":"comic"}).img.attrs
    comic_dict['num'] = x
    
    print comic_dict