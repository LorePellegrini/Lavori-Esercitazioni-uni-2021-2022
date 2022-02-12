#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 16:36:36 2022

@author: lorenzopellegrini
"""

n1= int(input('Inserisci un numero '))
n2= int(input('Inserisci un nunero '))

i=1
while i<=n1 and i<=n2:
    if n1%i==0 and n2%i==0:
        print(i)
    i=i+1