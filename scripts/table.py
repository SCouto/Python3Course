# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys


if len(sys.argv) >=  3 :

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    if num1 < 1 or num1 > 9 or num2 < 1 or num2 > 9:
        print ("Error, los numeros introducidos deben estar entre 1 y 9")
    else: 
        for i in range(num1):
            print("")
            for j in range(num2):
                print(" * ", end=''),
            
else :     
    print ("Error, insuficiente numero de parametros recibidos")   
     



    

