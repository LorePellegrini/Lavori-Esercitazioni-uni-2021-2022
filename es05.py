#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 17:21:30 2022

@author: lorenzopellegrini
"""

nr = 4 #numero di righe visualizzate
riga = 1 #contatore che cicla sulle righe
i=1 #contatore per ciclare su tutti i numeri del triangolo

while riga<=nr: #creo una riga del triangolo di floyd
    s='' #stringa vuota
    k=0 #utilizzo un secondo ciclo, permette capire quanti elementi da aggiungere alla riga
    while k<riga:
        s=s+'%3d   ' %(i) #inserimento di numeri in coda alla riga s con sistemazione della formattazione
        i=i+1 #permette di scalare lungo i numeri
        k=k+1 #lo aggiorno per far aumentare la lunmghezza delle righe
    print(s)
    riga=riga+1