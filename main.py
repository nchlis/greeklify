#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 15:58:01 2021

@author: nikos
"""


from itertools import chain
import shutil
import os
import pandas as pd
import glob
import numpy as np

def greeklify_str(str_in):
    str_out = []
    for c in str_in:
        if c in df['greek'].tolist():#convert
            str_out.append(df['greeklish'].loc[df['greek']==c].values[0])
        else:#leave as-is
            str_out.append(c)
    #join list of characters into a single string
    str_out = ''.join(str_out)
    return(str_out)

input_folder = './data/'

#% get all letters
df = pd.read_csv('./map.csv')

#%% read directories

input_filenames = []
for filename in glob.iglob(input_folder+'**/', recursive=True):
     # print(filename)
     input_filenames.append(filename)
     
#the first file is the input_folder
input_filenames = input_filenames[1:]
# print(input_filenames)

#%% rename directories

print('*renaming directories*')
for f in input_filenames:
    print('renaming',f)
    print('to:',greeklify_str(f))
    os.rename(f,greeklify_str(f))
    
#%% read files

input_filenames = []
for filename in glob.iglob(input_folder+'**/*', recursive=True):
    if os.path.isdir(filename) == False:
        # print(filename)
        input_filenames.append(filename)

#%% rename files

print('*renaming files*')
for f in input_filenames:
    print('renaming',f)
    print('to:',greeklify_str(f))
    os.rename(f,greeklify_str(f))

#output
# *renaming directories*
# renaming ./data/τεστ/
# to: ./data/test/
# *renaming files*
# renaming ./data/αρχείο1.txt
# to: ./data/arxeio1.txt
# renaming ./data/αρχείο2.txt
# to: ./data/arxeio2.txt
# renaming ./data/test/αρχείο1.txt
# to: ./data/test/arxeio1.txt
           