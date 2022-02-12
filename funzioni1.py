#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 18:34:36 2021

@author: lorenzopellegrini
"""

def main():
    startup_message()
    input('Premere invio per visualizzare il passaggio 1.')
    step1()
    input('Premere invio per visualizzare il passaggio 2.')
    step2()
    input('Premere invio per visualizzare il passaggio 3.')
    step3()
    input('Premere invio per visualizzare il passaggio 4.')
    step4()
    
def startup_message():
    print('Questo programma spiega come')
    print("disassemblare un'asciugatrice Acme.")
    print('Il processo richiede 4 passaggi')
    print()
    
def step1():
    print("Passaggio 1: staccare l'asciugatrice")
    print('dalla corrente e allontanarla dal muro')
    print()
    
def step2():
    print('Passaggio 2: togliere le sei viti')
    print("dal retro dell'asciugatrice")
    print()
    
def step3():
    print('Passaggio 3: rimuovere il pannello posteriore')
    print("dell'asciugatrice")
    print()
    
def step4():
    print('Passaggio 4: sollevare il pannello superiore')
    print("dell'asciugatrice")
    print('Congratulazioni, avete smontato la vostra asciugatrice')
    print('Ora potete riporla nella sua confezione')
    
main()