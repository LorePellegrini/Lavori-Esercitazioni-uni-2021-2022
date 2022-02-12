#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 22:03:51 2021

@author: lorenzopellegrini
"""

print('Inserire le coordinate cartesiane del punto P:')
x = float(input('ascissa  x = '))
y = float(input('ordinata y = '))
if x>0 and y>0:
    print('Il punto P appartiene al primo quadrante')   
if x<0 and y>0:
    print('Il punto P appartiene al secondo quadrante')   
if x<0 and y<0:
    print('Il punto P appartiene al terzo quadrante')
else:
  if x>0 and y<0:
   print('Il punto P appartiene al quarto quadrante')


   

    
  
  