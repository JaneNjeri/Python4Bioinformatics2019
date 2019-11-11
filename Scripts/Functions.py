def percenAT_GC(seq:str) -> tuple:    
    """ Function calculates percentage AT and GC content, given a DNA sequence. """    
    A_count=seq.count('A')
    C_count=seq.count('C')
    G_count=seq.count('G')
    T_count=seq.count('T')
    perc_GC = (G_count + C_count)/len(dna)*100
    perc_AT = (A_count + T_count)/len(dna)*100
    
    return perc_GC, perc_AT
    
    
def search_amino (seq:str):
    """ The function finds the first, last and fifth amino acids, given an amino acid sequnce. """
    for amino in seq:
        print(seq[0])
        print(seq[-1])
        print(seq[4])
        break
    return
    
    
def search_restr_site (seq:str):
    """ Function finds specific restriction sites based on index values in a DNA sequence. """
    print('The restriction site is at index %s' % seq.find('site'))
    return
    
    
def reverse_complement (seq:str):
    """ This function gets the reverse complement of given DNA sequences. """
    complement = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
    reverse_comp = "".join(complement[i] for i in seq[::-1])
    
    return reverse_comp


def percentageGC(seq):
    """ Function calculates percentage GC content of a DNA sequence. """
    per_gc = ((seq.count('G') + seq.count('C'))) / len(seq)*100         
    return (per_gc)
    
    
def isValidDNA(seq):
    """ Function checks if a DNA sequence is valid or not valid and at which position. """
    valid_bases = list('ACGT')
    valid = True
    for base in seq:
        if base in valid_bases:
            continue
        else:
            valid = False
            print("Invalid base %s at position %d" % (base, seq.find(base)))
    return(valid)
    
    
def percentageGC(seq):
    """ This function calculates percentage GC content for a valid DNA, and outputs validation for an invalid
        DNA sequence. """
    if isValidDNA(seq) == True:
        per_gc = ((seq.count('G') + seq.count('C'))) / len(seq)*100
        return(per_gc)
    else:
        print("Enter a valid DNA")
        
    return per_gc
    
    
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