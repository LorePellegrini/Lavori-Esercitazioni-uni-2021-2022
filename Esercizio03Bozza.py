#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 18:15:07 2021

@author: lorenzopellegrini
"""
tasso1 = 0.0083 #(ho diviso 0.5 per 60 minuti per trovare il costo al minuto)
tasso2 = 0.1667

print('inserire la durata in minuti della sosta')
t = int(input('durata della sosta: '))
if t<=30:
    print('La sosta è gratuita')
else: 
    if 31<t<=120:
       print('Il costo della sosta è di 1€')

if 121<t<=360:
      costo = 1+(t*tasso1)
      print('Il costo della sosta è di', costo, '€')
else:
    if t>360:
     costo2 = 1+(t*tasso2)
       if  1+(t*tasso2)>16:
    print('Il costo della sua sosta è di 16€')
else:    print('Il costo della sosta è di', costo2, '€')