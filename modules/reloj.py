#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 10:50:09 2019

@author: couto
"""

from os import system
from time import sleep
import datetime

currentSeconds = -1



while True:
    
    now = datetime.datetime.now()
    if (now.second != currentSeconds):
        currentSeconds = now.second
        print("{:02d}:{:02d}:{:02d}".format(now.hour, int(now.minute), int(currentSeconds)))
 
    now = datetime.datetime.now()
    print("{:02d}:{:02d}:{:02d}".format(now.hour, int(now.minute), int(currentSeconds)))
    sleep(1)
    system("clear")



    
