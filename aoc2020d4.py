# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 09:36:56 2020

@author: user
"""


import os
os.getcwd()
os.chdir("./aoc2020")

file="inputd4.txt"
f=open(file).read().split("\n\n")
for line in f:
    passport =line.split()
    print(passport)
