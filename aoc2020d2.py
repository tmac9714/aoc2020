# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 09:36:13 2020

@author: user
"""

import os
os.getcwd()
os.chdir("../aoc2020")

file = "inputd2.txt"

counter1 = 0
counter2 = 0
with open(file) as fp:
    for line in fp:
        nm,word,strs=line.split()
        n,m=nm.split('-')
        n,m=int(n),int(m)
        word=word.strip(':')
        if strs.count(word)<=m and strs.count(word)>=n:
            counter1 += 1
        if strs[n-1]==word and strs[m-1]!=word:
            counter2 += 1
        if strs[n-1]!=word and strs[m-1]==word:
            counter2 += 1
print(counter1)             
print(counter2)



            