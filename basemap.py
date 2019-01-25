# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 17:08:46 2019

@author: user
"""

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import os
os.environ["PROJ_LIB"]="C:\Users\user\Anaconda2\Library\share"
from mpl_toolkits.basemap import Basemap



plt.figure(figsize=(8, 8))
m = Basemap(projection='ortho', resolution=None,  lat_0=20.593683, lon_0=78.962883)
m.bluemarble(scale=0.5);






#plotting india
fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution=None,
            width=8E6, height=8E6, 
            #latitude and longitude
            lat_0=20.593683, lon_0=78.962883,)
m.etopo(scale=0.5, alpha=0.5)
# Map (long, lat) to (x, y) for plotting
x, y = m(75, 25)
plt.plot(x, y, 'ok', markersize=5)
#name and font size
plt.text(x, y, ' INDIA', fontsize=12);






from itertools import chain

def draw_map(m, scale=0.2):
    # draw a shaded-relief image
    m.shadedrelief(scale=scale)
    
    # lats and longs are returned as a dictionary
    lats = m.drawparallels(np.linspace(-90, 90, 13))
    lons = m.drawmeridians(np.linspace(-180, 180, 13))

    # keys contain the plt.Line2D instances
    lat_lines = chain(*(tup[1][0] for tup in lats.items()))
    lon_lines = chain(*(tup[1][0] for tup in lons.items()))
    all_lines = chain(lat_lines, lon_lines)
    
    # cycle through these lines and set the desired style
    for line in all_lines:
        line.set(linestyle='-', alpha=0.3, color='w')
        
        
        
        
        
fig = plt.figure(figsize=(8, 6), edgecolor='w')
m = Basemap(projection='cyl', resolution=None,
            llcrnrlat=-90, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180, )
draw_map(m)





fig = plt.figure(figsize=(8, 6), edgecolor='w')
m = Basemap(projection='moll', resolution=None,
             lat_0=20.593683, lon_0=78.962883)
draw_map(m)






fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='ortho', resolution=None,
             lat_0=20.593683, lon_0=78.962883)
draw_map(m);






fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution=None,
            lat_0=27.391277, lon_0=73.432617, lat_1=75, lat_2=85,
            width=1.6E7, height=1.2E7)
draw_map(m)







fig, ax = plt.subplots(1, 2, figsize=(12, 8))

for i, res in enumerate(['l', 'h']):
    m = Basemap(projection='gnom', lat_0=57.3, lon_0=-6.2,
                width=90000, height=120000, resolution=res, ax=ax[i])
    m.fillcontinents(color="#FFDDCC", lake_color='#DDEEFF')
    m.drawmapboundary(fill_color="#DDEEFF")
    m.drawcoastlines()
    ax[i].set_title("resolution='{0}'".format(res));
    
    
    
    
import pandas as pd
cities = pd.read_csv("C:\\Users\\user\\OneDrive\\Desktop\\rajasthan.csv")

# Extract the data we're interested in
lat = cities['lat'].values
lon = cities['lon'].values
population = cities['POPULATION'].values
area = cities['AREA_SQ_KM'].values



# 1. Draw the map background
fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution='h', 
            lat_0=37.5, lon_0=-119,
            width=1E6, height=1.2E6)
m.shadedrelief()
m.drawcoastlines(color='gray')
m.drawcountries(color='gray')
m.drawstates(color='gray')

# 2. scatter city data, with color reflecting population
# and size reflecting area
m.scatter(lon, lat, latlon=True,
          c=np.log10(population), s=area,
          cmap='Reds', alpha=0.5)

# 3. create colorbar and legend
plt.colorbar(label=r'$\log_{10}({\rm population})$')
plt.clim(3, 7)

# make legend with dummy points
for a in [100, 300, 500]:
    plt.scatter([], [], c='k', alpha=0.5, s=a,
                label=str(a) + ' km$^2$')
plt.legend(scatterpoints=1, frameon=False,
           labelspacing=1, loc='lower left');
         
           

           
           
from netCDF4 import Dataset
data = Dataset('gistemp250.nc')




from netCDF4 import date2index
from datetime import datetime
timeindex = date2index(datetime(2014, 1, 15),
                       data.variables['time'])




lat = data.variables['lat'][:]
lon = data.variables['lon'][:]
lon, lat = np.meshgrid(lon, lat)
temp_anomaly = data.variables['tempanomaly'][timeindex]