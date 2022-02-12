#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 10:17:26 2022

@author: lorenzopellegrini
"""

    
print('stampa a video i numeri dispari nell intervallo [0, 2000]')
cont=0 #contatore per quanti numeri divisibili per 3 incontrati
num=0
while num<2000:
    if num % 3 == 0:
        print((num))
        cont = cont + 1
    else:
        pass
    num = num + 1
print('fine')