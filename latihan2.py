#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 21:28:06 2020

@author: taufiq
"""

total = 0
for x in range(7):
    total = total + int(input("masukan bilangan: "))
    total = total > total

print ("bilangan terbesar adalah: ",total)