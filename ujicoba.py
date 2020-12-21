#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:14:21 2020

@author: taufiq
"""

a = " Hello, World! "
print(a.strip())

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.replace("W", "J"))

a = "Hello, World!"
c = a.split(",")
print(c)

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) 
