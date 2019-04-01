#!/usr/bin/python3
# Author:   J. Cameron Atkins
# Email:    atkinsjc23@gmail.com

import numpy as np
import argparse
import subprocess as sp
import socket 
import select 
import sys 
#from thread import *
class player:
    #Global
    hit_pts = 50

    def __init__(self,vertices):
        dd#vertices is a list where each entry is a list
        self.V= vertices
        self.graph = defaultdict(list)
        self.Time = 0


if __name__ == "__main__":
    
    while input():
        resp = input()
        print(resp)
        if resp == 'done':
            break
        else:
            print('received and...')
            print('next')




