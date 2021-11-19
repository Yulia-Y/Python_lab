# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 22:29:41 2021

@author: gasan
"""

def partial_sums(*a):
    res = [0]
    for i in range(len(a)):
        res.append(res[i] + a[i])
    return res
print(partial_sums(1,2,3,4,5,6,7))