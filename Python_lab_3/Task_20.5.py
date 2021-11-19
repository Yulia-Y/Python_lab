# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 22:12:57 2021

@author: gasan
"""

def happy(s):
    if len(s)<6:
        s=s+('0'*(6-len(s)))
    if sum([int(char) for char in s[:3]]) == sum([int(char) for char in s[-3:]]):
        print("Счастливый")
    else:
        print("Обычный")
 
if __name__ == '__main__':
    s = input()
    happy(s)
