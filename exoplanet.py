# -*- coding: utf-8 -*-
"""
Created on Mon May  3 13:06:32 2021

@author: Ákos Schméhl
"""

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# we need the calendar module for this one
import calendar

exoplanet= pd.read_csv('cumulative.csv')

#temporarily filling null values of date_added with unknown later to be replaced with logical value
exoplanet.kepler_name.fillna("unknown",inplace= True)

#dropping score data(excluding kepler score)
exoplanet.drop(exoplanet.iloc[:, 7:50], inplace = True, axis = 1)