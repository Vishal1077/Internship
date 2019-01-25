# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 17:07:36 2019

@author: user
"""

from bs4 import BeautifulSoup
import requests
import unicodedata



#specify the url
web = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

source = requests.get(web).text
soup = BeautifulSoup(source)



print (soup.prettify())

all_tables=soup.find_all('table')

print (all_tables)

right_table=soup.find('table', class_='table')

print (right_table)

A=[]
B=[]
C=[]
D=[]
E=[]

for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==5: #Only extract table body not heading
        A.append(str(cells[0].find(text=True)))
        B.append(str(cells[1].find(text=True)))
        C.append(str(cells[2].find(text=True)))    
        D.append(str(cells[3].find(text=True)))
        E.append(str(cells[4].find(text=True)))


import pandas as pd
        
df=pd.DataFrame()
df['Pos']=A
df['Team']=B
df['Weighted Matches']=C
df['Points']=D
df['Rating']=E

df.to_csv("Team_Ranking.csv")