#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import sys
import glob
import shutil
import datetime


def get_date(date):
    date_str = date.split('(')[0]
    date_strs = date_str.split('/')
    return datetime.date(int(date_strs[0]), int(date_strs[1]), int(date_strs[2]))


date = '2016/12/05(木)'
print(get_date(date))
