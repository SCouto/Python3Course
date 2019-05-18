#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:09:46 2019

@author: couto
"""

import random
import math

def leer_numero(ini, fin, mensaje):
    
    introducido = int(input("{}".format(mensaje)))
            
    
    while introducido < ini:
        introducido = int(input("{}".format(mensaje)))
    else:
        return introducido
    
def generador():
    numero = leer_numero(1, 20, "¿Cuantos números quieres generar? [1-20]:")
    modo = leer_numero(1, 3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")
    
    randomNumbers = []
    for i in range(numero):
        floatNumber = random.uniform(0,100)
        
        if modo == 1:
            finalNumber = math.ceil(floatNumber)
        elif modo == 2:
            finalNumber = math.floor(floatNumber)
        else:
            finalNumber = round(floatNumber)
        
        print("Original number: {}, Rounded number {}".format(floatNumber, finalNumber))
        randomNumbers.append(finalNumber)
        
    return randomNumbers

print(generador())
