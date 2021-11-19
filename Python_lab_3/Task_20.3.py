# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 22:02:19 2021

@author: gasan
"""
def print_only_new(data, lst):
    if data not in lst:
        print(data)
        lst.append(data)
lst = []
data = input()
print_only_new(data, lst)

