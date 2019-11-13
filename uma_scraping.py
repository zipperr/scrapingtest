# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import pandas
import os
import shutil
import sys
import glob
import time

url = 'https://race.netkeiba.com/?pid=race&id=p'
id = '2009010101'

filename = '2009010101.csv'
df = pandas.DataFrame()
df_all = pandas.DataFrame()

for i in range(1, 20):
    try:
        html = urllib.request.urlopen(url + str(id) + str(i).zfill(2)).read()
        df = pandas.read_html(html)[0]
        df['race_id?'] = str(i).zfill(2)
        df_all = df_all.append(df)
    except Exception as e:
        print(e)
        continue
df_all.to_csv(filename, index=False)
