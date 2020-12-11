# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 09:36:56 2020

@author: user
"""

import re
import os
os.getcwd()
os.chdir("./aoc2020")

file="inputd4.txt"

requirements={"byr","iyr","eyr","hgt","hcl","ecl","pid"}
#re_all={"byr","iyr","eyr","hgt","hcl","ecl","pid","cid"}

re2={"byr": lambda v : v>=1920 and v<=2002,
 "iyr": lambda v : v>=2010 and v<=2020,
 "eyr": lambda v : v>=2020 and v<=2030,
 "hgt": lambda v :(v.endswith("cm") and v>=150 and v<=193) or
 (v.endswith("in") and v>=59 and v<=76),
 "hcl": lambda v : re.match("^#[0-9a-f]{6}",v) ,
 "ecl": lambda v : v in ["amb","blu","brn","gry","grn","hzl","oth"],
 "pid": lambda v : len(v)==9}    


f=open(file).read().split("\n\n")
passports =[]
for group in f:
    passport =group.split()
    dictr = {item.split(":")[0]:item.split(":")[1] 
 for item in passport}
    #for item in passport:
        #key = item.split(":")[0]
        #value = item.split(":")[1]
        #dictr[key]=value
    passports.append(dictr)
print(passports)

# all 1個False，全部都是False
valid=0
valid2=0
for passport in passports:
    if all(r in passport for r in requirements):
    #if passport.keys()==requirements or passport.keys()==re_all:
        valid +=1
        if re2.values()==passport.values():
            
        
print(valid)
print(valid2)


        

