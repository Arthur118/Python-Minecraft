# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:05:30 2019

@author: Arthur
"""

import requests
from bs4 import BeautifulSoup

resp = requests.get('https://jwlin.github.io/py-scraping-analysis-book/ch1/connect.html')
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup.find('h1').text)
