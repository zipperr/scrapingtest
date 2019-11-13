# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import pandas
import os
import shutil


def get_common_info(html, df):
    s_soup = BeautifulSoup(html)
    race_div = s_soup.find("div", class_="mainrace_data fc")
    race_num_dt = race_div.find('dt')
    race_num = race_num_dt.text.replace('R', '').replace('\n', '')
    race_h1 = race_div.find('h1')
    race_name = race_h1.text
    race_div_p = race_div.find_all('p')
    course_detail_p = race_div_p[0]
    course_detail = course_detail_p.text
    condition_p = race_div_p[1]
    race_condition = condition_p.text
    date_p = race_div_p[2]
    race_date = date_p.text
    race_category_p = race_div_p[3]
    race_category = race_category_p.text
    return df


def scraping(url, filename):
    html = urllib.request.urlopen(url).read()
    try:
        df = pandas.read_html(html)[0]
        print(f'OK: {url}')
    except Exception as e:
        print(f'NoTable: {url}')
        print(e)

    df = get_common_info(html, df)
    df.to_csv(filename, index=False)
    print('プログラムが正常に終了しました')


# クレイピングCSVを作成
scraping('https://race.netkeiba.com/?pid=race&id=p200901010102', '200901010102.csv')
