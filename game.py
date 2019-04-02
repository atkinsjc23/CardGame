#!/usr/bin/python3
# Authors:   J. Cameron Atkins
#            Caleb Davis

import socket 
import sys 
import random
import player

if __name__ == "__main__":
    while True:
        resp = input()
        print(resp)
        if resp == 'done':
            break
        else:
            print('received and...')
            print('next')
