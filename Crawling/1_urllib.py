import requests
from bs4 import BeautifulSoup as bs


url = "http://api.aoikujira.com/ip/ini"
res = requests.get(url)
soup = bs(res.content, "html.parser")

print(soup)







#!/usr/bin/env pyton3

import sys


