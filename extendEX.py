#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 11:21:09 2022

@author: lorenzopellegrini
"""

CARDINALITA = 10
serie = []
serie2 = ['terzultimo', 'penultimo', 'ultimo']
i=0
while i < CARDINALITA: 
    numero=input('inserisci un numero ')
    serie.append(numero)
    print(serie)
    i += 1
serie.extend(serie2)
print(serie)