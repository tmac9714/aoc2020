# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 09:36:13 2020

@author: user
"""
import os
os.getcwd()
os.chdir("./aoc2020")

file = "inputd3.txt"

x=0
counter=0
with open(file) as fp:
    for line in fp:
        line=line.strip()
        #print(line[x%len(line)])
        if line[x%len(line)]=='#':           
            counter +=1
        x +=3     
print(counter)      

v=0
w=0
x=0
y=0
z=0
a=0
b=0
c=0
d=0
e=0
f=0
linenum=1
with open(file) as fp:
    
    for line in fp:
        line=line.strip()
        if line[w%len(line)]=='#':           
            a +=1
        w +=1
        if line[x%len(line)]=='#':           
            b +=1
        x +=3
        if line[y%len(line)]=='#':           
            c +=1
        y +=5
        if line[z%len(line)]=='#':           
            d +=1
        z +=7
        if linenum%2==1 :            
            if line[v%len(line)]=='#':                
                e +=1
            v +=1
        linenum += 1
print(a*b*c*d*e)
#############################
file = "inputd3.txt"

def treenum(right, down=1):
    counter=0
    x=0
    #y=0
    f=open(file,'r')
    for y,line in enumerate(f):
        line=line.strip()
        if y%down==0:
            if line[x%len(line)]=='#':
                counter +=1
            x += right    
        #y += 1                  
    return counter
print(treenum(3))
print(treenum(1)*treenum(3)*treenum(5)*treenum(7)*treenum(1,2))

###############

