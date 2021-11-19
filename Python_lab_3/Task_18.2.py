# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 12:53:38 2021

@author: gasan
"""

def ask_password():
    par = "password"
    kp=0
    while True:
        d = input()
        kp += 1
        if d == par and kp <= 3:
                print("Пароль принят")
                kp += 3
        elif kp == 3:
                print("В доступе отказано")
    