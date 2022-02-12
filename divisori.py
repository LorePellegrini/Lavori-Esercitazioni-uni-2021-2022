#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 18:22:22 2022

@author: lorenzopellegrini
"""

n1 = int(input('Inserisci il primo numero '))
n2 = int(input('Inserisci il secondo numero '))

i = 1
while i <= n1 and i <= n2:
    if n1%i == 0 and n2%i == 0:
        print(i)
    i = i + 1