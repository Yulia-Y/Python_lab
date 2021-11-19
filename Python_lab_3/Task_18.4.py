# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 13:14:21 2021

@author: gasan
"""

def bracket_check(test_string):
    result = 0
    for a in test_string:
        if "(" in a:
            result +=1
        elif ")" in a:
            result -= 1
        else:
            return "NO"
 
        if result < 0:
            return"NO"
    if result > 0:
        return"NO"
    return "YES"
