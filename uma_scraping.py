# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import pandas
import os
import shutil
import sys
import glob
import time

url = 'https://race.netkeiba.com/?pid=race&id=p200901010102'
filename = '200901010102.csv'

html = urllib.request.urlopen(url).read()
df = pandas.read_html(html)[0]
df.to_csv(filename, index=False)
