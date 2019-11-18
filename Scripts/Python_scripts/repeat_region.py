#! /home/user/miniconda3/bin/python

""" 
Function finds a particular base that is highly repeated 
and its lenght given a DNA sequence 
Usage:
    python repeat_region.py <seq_file> 

"""

import sys

seq_file = sys.argv[1]

def repeat_region(seq_file):
    nucs = set('ACGTCAGTGCAGTCAGT')
    A_list = []
    tag = False
    As = []
    for nuc in nucs:
        for dna in 'ACGTCAGTGCCCCCCCCCCCCCCCCCCCCCAGTCAGTTTTTAAAAAG':
            if dna == nuc:
                tag = True
                As.append(dna)
            else:
                if len(As) > 1:
                    A_list.append(As)
                As = []
                tag = False

    len_list = [len(x) for x in A_list]
    long_index = len_list.index(max(len_list))
    print("%s is the longest repeating letter, repeats %d times" % (
        A_list[long_index][0], len(A_list[long_index])))
    return A_list

if len(sys.argv) <2:
    print(_Doc_)
else:
    print()
    seq_file = sys.argv[1]
    
    
    
    
    
def find_ATG(seq):
    """ Function finds 'ATG' in a given sequence """
    DNA=input('DNA seq:\n')
    start=0
    while DNA.find('ATG',start) !=-1:
        found=DNA.find('ATG',start)
        start=found+1
        print(found)
    return seq