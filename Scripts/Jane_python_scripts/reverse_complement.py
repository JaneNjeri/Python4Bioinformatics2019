#! /home/user/miniconda3/bin/python

""" 
This function gets the reverse complement 
of given DNA sequences
Usage:
    python reverse_complement.py <seq_file> 

"""

import sys

seq_file = sys.argv[1]

def reverse_complement (seq_file:str):
    complement = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
    reverse_comp = "".join(complement[i] for i in seq[::-1])
    
    return reverse_comp

if len(sys.argv) <2:
    print(_Doc_)
else:
    print()
    seq_file = sys.argv[1]
