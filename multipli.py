#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 18:13:51 2022

@author: lorenzopellegrini
"""

ls = int(input('Limite superiore (>2)?'))
i = 2 
while i < ls:
    if i%7==0 or i%9==0:
        print(i)
    i=i+1