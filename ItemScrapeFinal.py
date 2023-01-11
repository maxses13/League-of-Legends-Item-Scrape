# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 13:15:29 2023

@author: maxdi
"""

import requests
import pandas as pd
from pandas.io.json import json_normalize
import json

#Sends request to url
url = "http://ddragon.leagueoflegends.com/cdn/13.1.1/data/en_US/item.json"
R = requests.get(url)

#Save file from url as json file
name = R.json()

#This normalizes all data into pandas dataframe based on json
name = pd.json_normalize(name["data"].values())
 
#This removes unneeded columns
name = name.drop(columns=['into','image.full','image.sprite','image.group','image.x','from','image.y','image.w','image.y','image.h','inStore','maps.21','maps.22','specialRecipe','stacks','requiredAlly','colloq'])

#This removes HTML tags from description, making it easier to read
name['description'] = name['description'].str.replace(r'<[^<>]*>', '', regex=True)

#Filters dataframe for only items containing purchasable = True
name = name[name['gold.purchasable'] == True]

#Save final datafram to csv for excel
name.to_csv('LeagueItemsFinal1.csv', index=False)
