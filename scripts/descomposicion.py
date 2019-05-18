#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 15:47:12 2019

@author: couto
"""
import sys

if len(sys.argv) >=  2:
    
    s = sys.argv[1][::-1]
    l = len(s)
    
    for i, c in enumerate(s):
        n = int(c)
        print("{:04d}".format(n*10 ** i))
        
    
    
    
else:
    print("Debe recibirse un parametro")