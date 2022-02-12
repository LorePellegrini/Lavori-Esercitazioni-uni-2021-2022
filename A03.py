#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 10:54:52 2022

@author: lorenzopellegrini
"""

print('Inserire la data:')
g=int(input('Inserisci il giorno: '))
m=int(input('Inserisci il mese: '))
a=int(input("Inserisci l'anno: "))

while g<= 31 and m <=12:
    if g <= 30 and m == 11 and m== 4 and m== 6 and m==9:
        print('La data è plausibile')
    elif g<= 31 and m!=11 and m!= 4 and m!=6 and m!=9:
        print('La data  è plausibile')
    elif g>=28 and m==2:
        print('La data non è plausibile')
else:
 print('La data non è plausibile')
