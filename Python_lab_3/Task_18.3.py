# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 17:26:08 2021

@author: gasan
"""
def fib ( i) :
    if i==0 or i==1:
        return 1
    else:
        return i+fib(i-1)
def golden_ratio( i):
    return fib(i)/fib(i-1)
print(golden_ratio(int(input())))