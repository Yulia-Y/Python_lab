# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 22:05:59 2021

@author: gasan
"""

def hello(temp):
    print("Hello,", temp, " !We are trying to find ur card...")
 
 
def search_card(temp):
    if temp in base:
        print("We have found ur card with ",base.index(temp)+1," number!")
    else:
        print("We doesnt found ur card...")

if __name__ == '__main__':
    base = ["Иван", "Юлия Иванкова"]
    hello("Иван")
    search_card("Иван")
    hello("Юлия Иванова")
    search_card("Юлия Иванова")