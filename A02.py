#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 10:43:14 2022

@author: lorenzopellegrini
"""

n = int(input('Inserisci un numero: '))
if n<0:
    print('Il fattoriale non esiste')
    
elif n == 0:
    print('Il fattoriale è 1')
    
else:
    i=n-1
    while i >= 1 :
        n=i*n
        i=i-1
        print('Il fattoriale è', n,)
        
