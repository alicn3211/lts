#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:47:18 2019

@author: ali
"""

from multiprocessing import Process
import os
from signal import *
from time import sleep




def saler_handler(sig,frame):
    if sig ==SIGINT:
        os.kill(os.getppid(),SIGUSR1)
        
    elif sig == SIGQUIT:
        os.kill(os.getppid(),SIGUSR2)
    elif sig ==SIGUSR1:
        print('daozhan l qingxiache')
        os._exit(0)
        
def driver_handler(sig,frame):
    if sig == SIGUSR1:
        print('laosiji kaichele ')
    elif sig ==SIGUSR2:
        print('chesu youdiankuai xihaoanquandai')
    elif sig ==SIGTSTP:
        os.kill(p.pid,SIGUSR1)
        
def saler():
    signal(SIGINT,saler_handler)
    signal(SIGQUIT,saler_handler)
    signal(SIGUSR1,saler_handler)
    signal(SIGTSTP,SIG_IGN)
    while True:
        sleep(2)
        print('python dai ni qu yuan fang')
p = Process(target=saler)
p.start()
# FUJINCHEN
signal(SIGUSR1,driver_handler)
signal(SIGUSR2,driver_handler)
signal(SIGTSTP,driver_handler)
signal(SIGINT,SIG_IGN)
signal(SIGQUIT,SIG_IGN)


p.join()
