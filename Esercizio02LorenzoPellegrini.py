#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 17:36:25 2021

@author: lorenzopellegrini
"""

a = int(input('primo lato a = '))
b = int(input('secondo lato b = '))
c = int(input('terzo lato c = '))

if a>b+c or b>a+c or c>a+b:
    print('Errore! I tre valori non possono rappresentare i lati di un triangolo, poichè non rispettano la disuguaglianza triangolare')
            
else:
 if a<b+c or b<a+c or c<b+a:
  print('I valori inseriti possono rappresentare i lati di un triangolo')    