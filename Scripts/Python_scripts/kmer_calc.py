def getkmers(DNA,k):
    DNA = input('enter the DNA seq:\n')
    step= 0
    DNA_list=[]
    while step<=len(DNA)-k:
        DNA_list.append(DNA[step:step+k])
        step = step + 1
    return DNA_list