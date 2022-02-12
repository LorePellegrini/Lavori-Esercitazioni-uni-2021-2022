#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 16:28:12 2022

@author: lorenzopellegrini
"""

n=int(input('Inserisci un numero maggiore di 2: '))
i=2 #contatore per scorrere i numeri
while i<=n:
    if i % 7 == 0 or i % 9 == 0:
        print(i)
    i=i+1