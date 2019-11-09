#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 20:10:22 2019

@author: ali
"""

from multiprocessing import Thread
from time import sleep,ctime

class MyThread(Thread):
    def __init__(self,target,name='ali',\
                 args=(),kwargs = {}):
        super().__init__()
        self.name=name
        self.target=target
        self.args=args
        self.kwargs=kwargs
    def run(self):
        self.target(*self.args,**self.kwargs)

def player(song,sec):
    for i in range(2):
        print('Playing %s:%s'%(song,ctime()))
        sleep(sec)

t = MyThread(target = player,args=('liangliang',),kwargs={'sec':2})
t.start()
t.join()