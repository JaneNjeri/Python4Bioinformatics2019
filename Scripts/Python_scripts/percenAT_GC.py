#! /home/user/miniconda3/bin/python

""" 
Function calculates percentage AT and GC content, 
given a DNA sequence. 
Usage:
    python percenAT_GC.py <seq_file> 

""" 

import sys

seq_file = sys.argv[1]

def percenAT_GC(seq_file:str) -> tuple:    
       
    A_count=seq.count('A')
    C_count=seq.count('C')
    G_count=seq.count('G')
    T_count=seq.count('T')
    perc_GC = (G_count + C_count)/len(dna)*100
    perc_AT = (A_count + T_count)/len(dna)*100
    
    return perc_GC, perc_AT

if len(sys.argv) <2:
    print(_Doc_)
else:
    print()
    seq_file = sys.argv[1]
    