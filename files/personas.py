#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:29:23 2019

@author: couto
"""

from io import open

fichero = open('personas.txt','r', encoding="utf8")

lines = fichero.readlines() 
fichero.close()


for line in lines:    
    print(line)
    splittedLine = line.replace("\n", "").split(";")
    persona = {"id":splittedLine[0], "nombre":splittedLine[1], "apellidos":splittedLine[2], "nacimiento":splittedLine[3]}
    print(persona)