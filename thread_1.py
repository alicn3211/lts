#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 23:45:47 2019

@author: ali
"""

import threading
from time import sleep
import os


def music():
    for i in range(5):
        #sleep(2)
        print("play huluwa",os.getpid())
        
t = threading.Thread(target = music)
t.start()

for i in range(5):
    #sleep(1.5)
    print("play jay",os.getpid())
    

t.join()