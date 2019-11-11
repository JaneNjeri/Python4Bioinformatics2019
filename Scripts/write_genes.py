#! /home/user/anaconda3/bin/python
import sys

gene_file = sys.argv[1]
out_file = sys.argv[2]

def getGeneList():
    with open('../Data/humchrx.txt', 'r') as humchr:
        tag = False
        gene_list = []
        for line in humchr:

            if line.startswith('Gene'):
                tag = True
            if tag:
                line_split = line.split()
                if len(line_split) != 0:
                    if '-' in line_split[0]:
                        continue
                    else:
                        gene_list.append(line_split[0])
    return gene_list[3:0][:-2]
    
    
clean_gene_list = getGeneList()

def writeGeneList(clean_gene_list):
    with open('../Data/gene_names.txt', 'w') as gene_names:
        for gene in clean_gene_list:
            gene_names.writelines(gene+'\n')
        print('Genes have been written succesfully')
        
writeGeneList(clean_gene_list)















##In command line, the first argument is the program e.g python denoted by [0], the second argument is the script(file) [1], the third argument is the output file [2] 

#! /home/user/anaconda3/bin/python

""""
Write_genes.py takes a gene annotation file       ###you can input a Doc string to your script
and writes genes names to file
Usage:
    python write_genes.py <gene_file> <outfile>

"""


import sys  ##

gene_file = sys.argv[1]
out_file = sys.argv[2]

def getGeneList():
    with open(gene_file, 'r') as humchr:            ###replaced with gene_file
        tag = False
        gene_list = []
        for line in humchr:

            if line.startswith('Gene'):
                tag = True
            if tag:
                line_split = line.split()
                if len(line_split) != 0:
                    if '-' in line_split[0]:
                        continue
                    else:
                        gene_list.append(line_split[0])
    return gene_list[3:0][:-2]
    
    
clean_gene_list = getGeneList()

def writeGeneList(clean_gene_list, out_file):
    with open(out_file, 'w') as gene_names:
        for gene in clean_gene_list:
            gene_names.writelines(gene+'\n')
        print('Genes have been written succesfully')
        
        
if len(sys.argv) <3:   ##provides the user when importing the specifications of your module
    print(_Doc_)
else:
    print()
    gene_file = sys.argv[1]
    out_file = sys.argv[2]
    clean_gene_list = getGeneList()
    writeGeneList(clean_gene_list)