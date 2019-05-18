#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 10:03:58 2019

@author: couto
"""

def suma(a, b):
    try:
        r = a + b
    except TypeError:
        print("Error: Tipo de dato no valido")
    else:
        return r
    
def resta(a, b):
    try:
        r = a - b
    except TypeError:
        print("Error: Tipo de dato no valido")
    else:
        return r
    
def division(a, b):
    try:
        r =  a / b
    except TypeError:
        print("Error: Tipo de dato no valido")
    else:
        return r

def producto(a, b):
    try:
        r = a * b    
    except TypeError:
        print("Error: Tipo de dato no valido")
    except ZeroDivisionError:        
        print("Imposible dividir entre 0")
    else:
        return r
    
