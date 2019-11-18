#! /home/user/miniconda3/bin/python

import sys

""" 
Function calculates percentage GC content 
of a DNA sequence
Usage:
    python percentageGC.py <seq_file> 
"""
seq_file = sys.argv[1]

def percentageGC(seq_file):
    per_gc = ((seq.count('G') + seq.count('C'))) / len(seq)*100         
    return (per_gc)

if len(sys.argv) <2:
    print(_Doc_)
else:
    print()
    seq_file = sys.argv[1]



 
""" 
Function checks if a DNA sequence is valid 
or not valid and at which position
Usage:
    python isValidDNA.py <seq_file> 
"""
seq_file = sys.argv[1]

def isValidDNA(seq_file):
    valid_bases = list('ACGT')
    valid = True
    for base in seq:
        if base in valid_bases:
            continue
        else:
            valid = False
            print("Invalid base %s at position %d" % (base, seq.find(base)))
    return(valid)

if len(sys.argv) <2:
    print(_Doc_)
else:
    print()
    seq_file = sys.argv[1]
    



""" 
This function calculates percentage GC content for a valid DNA, 
and outputs validation for an invalid DNA sequence
Usage:
    python percentageGC.py <seq_file> 
"""
seq_file = sys.argv[1]

def percentageGC(seq_file):
    if isValidDNA(seq) == True:
        per_gc = ((seq.count('G') + seq.count('C'))) / len(seq)*100
        return(per_gc)
    else:
        print("Enter a valid DNA")
        
    return per_gc

if len(sys.argv) <2:
    print(_Doc_)
else:
    print()
    seq_file = sys.argv[1]