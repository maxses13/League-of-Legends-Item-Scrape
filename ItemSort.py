# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 17:11:14 2023

@author: maxdi
"""
import requests
import pandas as pd
from pandas.io.json import json_normalize
import json


url = "http://ddragon.leagueoflegends.com/cdn/12.23.1/data/en_US/item.json"
R = requests.get(url)

name = R.json()

pd.json_normalize(name)



data = name["data"]

bdata = pd.DataFrame.from_dict(data)