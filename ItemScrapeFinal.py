# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 13:15:29 2023

@author: maxdi
"""

import requests
import pandas as pd
from pandas.io.json import json_normalize
import json


url = "http://ddragon.leagueoflegends.com/cdn/12.23.1/data/en_US/item.json"
R = requests.get(url)

name = R.json()

name = pd.json_normalize(name["data"].values())
 
name = name.drop(columns=['into','image.full','image.sprite','image.group','image.x','from','image.y','image.w','image.y','image.h','inStore','maps.21','maps.22','specialRecipe','stacks','requiredAlly','colloq'])

name = name[name['gold.purchasable'] == True]
