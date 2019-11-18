#! /home/user/miniconda3/bin/python

import sys

def get_0to5_whileloop(number):
    """ Function uses a while loop to get numbers 1 to 5 given a certain figure """
    x = 0
    numbers_list=[]
    while x < 5:
        numbers_list.append(x+1)
        x += 1
    return numbers_list


def get_6to10whileloop(number):
    """ Function uses a while loop to get numbers 1 to 10,
    skipping 5 given a certain figure """
    x = 0
    while x < 10:
        x += 1
        if x == 5:
            continue
        print(x)
        
        
def get_4to10_forloop(number):
    """ Function uses a for loop to extract numbers from 4 to 10,
    given a range of numbers using indexing """
    x=0
    number = range(11)
    for x in number:
        if x<4:
            continue
        print(x)