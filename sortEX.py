#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 11:29:11 2022

@author: lorenzopellegrini
"""

CARDINALITA = 6
serie = []

i = 0
while i < CARDINALITA:
    numero = input('inserisci un numero ')
    serie.append(numero)
    print(serie)
    i += 1
serie.sort()
print(serie)