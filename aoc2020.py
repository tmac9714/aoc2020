# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 09:36:13 2020

@author: user
"""

import os
os.getcwd()

file = "inputd1.txt"
list = []
with open(file) as fp:
    for line in fp:
        list.append(int(line.strip()))

for i in list:
    for j in list:
        if i+j==2020:
            print(i*j)
            break
    
for i in list:
    for j in list:
        for k in list:
            if i+j+k==2020:
                print(i*j*k)
                break      