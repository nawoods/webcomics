# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

session = requests.session()
for x in range(39,4110):

    exec("req = session.get('http://explosm.net/comics/%s')" % (x))
    doc = BeautifulSoup(req.content, 'html.parser')
    result = doc.find("h3",{"class":"zeta small-bottom-margin past-week-comic-title"})
    if result:
        print result.string


