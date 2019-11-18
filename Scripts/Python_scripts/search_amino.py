#! /home/user/miniconda3/bin/python

""" 
The function finds the first, 
last and fifth amino acids, 
given an amino acid sequnce
Usage:
    python search_amino.py <seq_file> 
"""

import sys

seq_file = sys.argv[1]

def search_amino (seq_file:str):
    for amino in seq:
        print(seq[0])
        print(seq[-1])
        print(seq[4])
        break
    return

if len(sys.argv) <2:
    print(_Doc_)
else:
    print()
    seq_file = sys.argv[1]
    


""" 
Function finds specific restriction sites 
based on index values in a DNA sequence, 
given a restriction site
Usage:
    python search_restr_site.py <seq_file>
"""    

seq_file = sys.argv[1]

dna_seq = 'AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA'

def search_restr_site (seq_file:str):
    print('The restriction site is at index %s' % seq.find('TCCGGA'))
    return seq

if len(sys.argv) <2:
    print(_Doc_)
else:
    print()
    seq_file = sys.argv[1]
    