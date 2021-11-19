# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 17:44:21 2021

@author: gasan
"""
def line(s, t):
    x = float(t[:t.index(';')])
    y = float(t[t.index(';') + 1:])
    k = float(s[:s.index('x')])
    b = float(s[s.index('x') + 1:])
    print((k * x + b) == y)
line(input(),input())
