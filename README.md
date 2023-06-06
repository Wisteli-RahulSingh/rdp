# rdp


http://54.156.114.207/

import pandas as pd
import numpy as np
import time 
from tqdm import tqdm
tqdm.pandas()
import os
import json
import glob
from pandas import json_normalize

with open('data/LABADIE-440428-5427962/Vitals.json') as file:
    v = json.load(file)
    
   v1 = pd.json_normalize(v, max_level=0)
   
   def parseVitals(df, colName):
    v2 = df.explode(colName)
    cols = list(pd.json_normalize(v2[colName], max_level=1).columns)
    v2[cols] = pd.json_normalize(v2[colName], max_level=1)
    v2.drop(columns = [colName], inplace=True)
    return v2
    
    
   colList = ['patientVitals', 'observationSets', 'observationSegments']
   
   for col in colList: 
    v1 = parseVitals(v1, col)


git add notebook1.ipynb notebook2.ipynb notebook3.ipynb
