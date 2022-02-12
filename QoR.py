#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 10:03:24 2021

@author: lorenzopellegrini
"""

print('inseirire i valori dei lati')
a = int(input('lato 1 = '))
b = int(input('lato 2 = '))
c = int(input('lato 3 = '))
d = int(input('lato 4 = '))
if a == b == c == d == a and a != 0 and b != 0 and c != 0 and d != 0:
        print('la figura è un quadrato')
        perimetro = a*4
        area = a**2 
        print('perimetro = ', perimetro)
        print('area = ', area)
elif a == c and b == d and a != 0 and b != 0 and c != 0 and d != 0:
    print('la figura è un rettangolo')
    perimetro = (a+b)*2
    area = a*b
    print('perimetro', perimetro)
    print('area', area)
    
else:
    print('la figura non è nè un quadrato nè un rettangolo')
