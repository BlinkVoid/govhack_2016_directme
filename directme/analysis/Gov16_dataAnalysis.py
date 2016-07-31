
# coding: utf-8

# In[1]:

class Debug:
    def __init__(self, level):
        self.level = level
    def msg(self, level, m):
        if(level <= self.level):
            print(m)
debug = Debug(10).msg


# In[2]:

#!/usr/bin/python
#AWS redshift connector:
#setup
from datetime import date, timedelta
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt


# In[3]:

def uniqueSummary(csvname):
    df = pd.read_csv(csvname)
    newdf = pd.DataFrame(columns = df.columns)
    for colName in df.head():
        u = df[colName].unique()
        if len(u) > 100:
            newdf.loc[:, colName] = [len(u), "more than 100"]
        else:
            newdf.loc[:, colName] = [len(u), u]
    newdf = newdf.T
    
    newdf.to_csv("uniqueSummary_" + csvname)
        


# In[7]:

## don't run below if you have files in the prefix of uniqueSummary_*
with open("filenames.txt") as f:
    for i in f:
        i = i.strip('\n')
        uniqueSummary(i)
        


# In[4]:

class LOC():
    def __init__(self,lat, long):
        self.lat = lat
        self.long = long


# In[45]:

def getNodes(A, B): #(A, B, nodedf) #keep in mind this function assumes lat in negative values
    tempdf = nodedf[(nodedf['Lat'] <= A.lat) & (nodedf['Lat'] >= B.lat) &
                    (nodedf['Long'] <= B.long) & (nodedf['Long'] >= A.long) ]
    return tempdf


# ## Get the unique probability summary
# ### age composition, road surface conditions, road atmospheric conditions,

# In[8]:

#plot
def plotBarChart(data):
    fig, ax = plt.subplots()

    index = data.index
    bar_width = 0.35

    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    rects1 = plt.bar(index, data.values, bar_width,
                     alpha=opacity,
                     color='b',
                     error_kw=error_config,
                     label='age groups')

    plt.xlabel('Age groups')
    plt.ylabel('Accident counts')
    plt.title('Age vs accidents')
    plt.legend()
    #plt.tight_layout()
    plt.show()


# In[31]:

#get road surface condition
def getDetailDF(df1, df2, key, query): #df1 = inrangedf, df2 = which ever data we want to get with the same accident no
    tempdf = df2[df2[key].isin(df1[key])]
    tempdf = tempdf[query].value_counts()
    tempdf2 = tempdf / tempdf.sum()
    return (tempdf, tempdf2)


def get_long_lat(start,end,):
    pointA = LOC(start[0],start[1])
    pointB = LOC(end[0],end[1])

    inrangedf = getNodes(pointA,pointB)
    long_coords = pd.Series.tolist(inrangedf['Long'])
    lat_coords = pd.Series.tolist(inrangedf['Lat'])

    long_lat_coords = []
    n = 0
    while n < len(long_coords):
        long_lat_coords.append((lat_coords[n],long_coords[n]))
        n += 1

    return long_lat_coords


# In[ ]:

#for age: PERSON.csv
#for road surface: ROAD_SURFACE_COND.csv
#for road atmospheric conditions: ATMOSPHERIC_COND.csv
#checking against inrangenodedf
persondf = pd.read_csv("PERSON.csv")
roadSurfacedf = pd.read_csv("ROAD_SURFACE_COND.csv")
roadAtmosphericdf = pd.read_csv("ATMOSPHERIC_COND.csv")
nodedf = pd.read_csv("NODE.csv")
#preferrably load everything at server_start


# In[46]:

#tie everything together
pointA = (-37.800793, 144.8803823)
pointB = (-37.8622120,144.8831790)
#===========
 #the function assume the lat is in negative values. 
#[print pd.Series.tolist(inrangedf['Lat'])
print get_long_lat(pointA,pointB)

#injury distribution
#injuries1, injuries_pct = getDetailDF(inrangedf, persondf, "ACCIDENT_NO", "INJ_LEVEL")
#age distribution
#ages, ages_pct = getDetailDF(inrangedf, persondf, "ACCIDENT_NO", "AGE")
#plotBarChart(ages)
#get road surface conditions
#roadSurfaces, roadSurfaces_pct = getDetailDF(inrangedf, roadSurfacedf, "ACCIDENT_NO", "Surface Cond Desc")
#get atmospheric conditions
#roadAtmospherics, roadAtmospherics_pct = getDetailDF(inrangedf, roadAtmosphericdf, "ACCIDENT_NO", "Atmosph Cond Desc")


# In[48]:

#print(type(injuries))
#print(injuries1)
#print(type(ages))
#print(ages)
#print(roadSurfaces)
#print(roadSurfaces_pct)
#print(roadAtmospherics)
#print(roadAtmospherics_pct)


# In[ ]:



