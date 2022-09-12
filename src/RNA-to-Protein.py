'''NAME
       RNA-to-Protein

VERSION
        1.1

AUTHOR
        Hector Ulises Gaspar <hectorgasp@gmail.com>

DESCRIPTION
        Este script obtiene el peptido codificado por una secuencia de DNA o RNA dada por el usuario

CATEGORY
        Script

USAGE
         python RNA-to-Protein.py -s DNA/RNAsequece


ARGUMENTS
        none
    
SEE ALSO
        Ninguno

'''

import re

gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T',
    'ACC':'T', 'ACG':'T', 'ACT':'T', 'AAC':'N', 'AAT':'N',
    'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R',
    'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CAC':'H',
    'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R',
    'CGG':'R', 'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V',
    'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G',
    'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S', 'TCC':'S',
    'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L',
    'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}


def DNA_test(seq):
    try:
        if re.search("[^ATGCU]", seq):
            #Si no, se avisa al usuario que la secuencia no es valida
            raise ValueError
    except ValueError:
        print(f"La secuencia no es valida, contiene caracteres no identificados")
    else:
        seq = seq.replace("U", "T")
        return(seq)

'''
def Translation(dna, aminoacids):
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]

        if gencode[codon] == "_":
            break
        else:
            print(codon)
            aminoacids.append(gencode[codon])
            return(aminoacids)
'''

aminoacids = []
seq = input("Introduce tu secuencia de DNA o RNA: \n")
seq = seq.upper()


dna = DNA_test(seq)

#peptide = "".join(Translation.aminoacids)

#print("El peptido codificado por la secuencia es: " + peptide)

for i in range(0, len(seq), 3):
    codon = seq[i:i+3]

    if gencode[codon] == "_":
        break
    else:
        #print(codon)
        aminoacids.append(gencode[codon])

peptide = "".join(aminoacids)
print("El peptido codificado por la secuencia es: " + peptide)
