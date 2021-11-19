# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 17:32:32 2021

@author: gasan
"""

def equation(x1, y1, x2, y2):
    if (x2 - x1) !=0: 
        k = (y2 - y1) / (x2 - x1)
        b = y1 - x1 * k
        print(f'y = {k:.2f}*x {b:+.2f}')
    else:
        print(0)

St1=list(map(int, input().split(';')))
St2=list(map(int, input().split(';')))
equation(St1[0], St1[1], St2[0], St2[1])