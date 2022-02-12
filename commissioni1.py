#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 09:46:57 2021

@author: lorenzopellegrini
"""

keep_going = 's'

while keep_going == 's':
    sales = float(input('Inserire il totale delle vendite: '))
    comm_rate = float(input('Inserire la percentuale delle provvigioni: ')) / 100
    commission = sales * comm_rate
    print('Le provvigioni sono €', \
          format(commission, '.2f'), sep='')
    keep_going = input("Vuoi calcolare un'altra" + \
                           "provvigione? (inserisci s per Sì): ")