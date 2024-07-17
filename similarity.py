#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:55:45 2020

@author: arianayoum
"""

from scipy.io import loadmat
import pandas as pd
import itertools
import numpy as np
import csv
import statistics
import os

# set workingdir
os. chdir("/Users/arianayoum/Desktop/Outside Project/Pilot_data")

# read in data
#meadowsid = 'causal-kiwi'
#x = loadmat('Meadows_Kitchen_v_v7_' + meadowsid + '_3_1D.mat')

x = loadmat('Meadows_Word-Space_pilot_v_v2_3D (1).mat')

# view data
x 

dissimilarity = x['rdmutv']
items = np.char.strip(x['stimuli'])
items[0] = 'Fork'

def expandgrid(*itrs):
   product = list(itertools.product(*itrs))
   return {'Var{}'.format(i+1):[x[i] for x in product] for i in range(len(itrs))}

all_pairs = expandgrid(items,items)