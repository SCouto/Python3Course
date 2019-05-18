#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:37:12 2019

@author: couto
"""

from io import open

fileName = "contador.txt"

try:
    fichero = open(fileName, "r")
    cont = int(fichero.read())
    fichero.close()
except FileNotFoundError:
    cont  = 0
except ValueError:
    print("Fichero corrupto")
    cont = 0
    
fichero = open(fileName, "w")
arg = input("Introduzca argumento: ")

if arg == "inc":
    cont += 1
elif arg == "dec":
    cont -= 1

   
print (cont)
fichero.write(str(cont))