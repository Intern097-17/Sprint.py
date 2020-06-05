file open('dna.txt', 'r')
dna = file.read()

print "DNA Sequence: ", dna

# mRNA codon chart

protein = {
    'UUU':'Phe', 'UUC':'Phe', 'UUA':'Leu', 'UUG':'Leu',
    'CUU':'Leu', 'CUC':'Leu', 'CUA':'Leu', 'CUG':'Leu',
    'AUU':'Ile', 'AUC':'Ile', 'AUA':'Ile', 'AUG':'Met',
    'GUU':'Val', 'GUC':'Val', 'GUA':'Val', 'GUG':'Val',
    'UCU':'Ser', 'UCC':'Ser', 'UCA':'Ser', 'UCG':'Ser',
    'CCU':'Pro', 'CCC':'Pro', 'CCA':'Pro', 'CCG':'Pro',
    'ACU':'Thr', 'ACC':'Thr', 'ACA':'Thr', 'ACG':'Thr',
    'GCU':'Ala', 'GCC':'Ala', 'GCA':'Ala', 'GCG':'Ala',
    'UAU':'Tyr', 'UAC':'Tyr', 'UAA':'Stop', 'UAG':'Stop',
    'CAU':'His', 'CAC':'His', 'CAA':'Glu', 'CAG':'Glu',
    'AAU':'Asn', 'AAC':'Asn', 'AAA':'Lys', 'AAG':'Lys',
    'GAU':'Asp', 'GAC':'Asp', 'GAA':'Glu', 'GAG':'Glu',
    'UGU':'Cys', 'UGC':'Cys', 'UGA':'Stop', 'UGG':'Trp',
    'CGU':'Arg', 'CGC':'Arg', 'CGA':'Arg', 'CGG':'Arg',
    'AGU':'Ser', 'AGC':'Ser', 'AGA':'Arg', 'AGG':'Arg',
    'GGU':'Gly', 'GGC':'Gly', 'GGA':'Gly', 'GGG':'Gly' 
}

protein_sequence = ""

for i in range(0, len(dna)-(3+len(dna)%3)
if protein[dna[i:i+3]] == "Stop" :

    break

protein_sequence += protein[dna[i:i+3]]

# Print the protein

print "Protein Sequence: ", protein_sequence


inputfile ="DNA.txt"
f = open("DNA.txt", "r")
seq = f.read()

seq = seq.replace("\n", "")
seq = seq.replace("\r", "")

def translate(seq)

genetic_code = {
    'UUU':'Phe', 'UUC':'Phe', 'UUA':'Leu', 'UUG':'Leu',
    'CUU':'Leu', 'CUC':'Leu', 'CUA':'Leu', 'CUG':'Leu',
    'AUU':'Ile', 'AUC':'Ile', 'AUA':'Ile', 'AUG':'Met',
    'GUU':'Val', 'GUC':'Val', 'GUA':'Val', 'GUG':'Val',
    'UCU':'Ser', 'UCC':'Ser', 'UCA':'Ser', 'UCG':'Ser',
    'CCU':'Pro', 'CCC':'Pro', 'CCA':'Pro', 'CCG':'Pro',
    'ACU':'Thr', 'ACC':'Thr', 'ACA':'Thr', 'ACG':'Thr',
    'GCU':'Ala', 'GCC':'Ala', 'GCA':'Ala', 'GCG':'Ala',
    'UAU':'Tyr', 'UAC':'Tyr', 'UAA':'Stop', 'UAG':'Stop',
    'CAU':'His', 'CAC':'His', 'CAA':'Glu', 'CAG':'Glu',
    'AAU':'Asn', 'AAC':'Asn', 'AAA':'Lys', 'AAG':'Lys',
    'GAU':'Asp', 'GAC':'Asp', 'GAA':'Glu', 'GAG':'Glu',
    'UGU':'Cys', 'UGC':'Cys', 'UGA':'Stop', 'UGG':'Trp',
    'CGU':'Arg', 'CGC':'Arg', 'CGA':'Arg', 'CGG':'Arg',
    'AGU':'Ser', 'AGC':'Ser', 'AGA':'Arg', 'AGG':'Arg',
    'GGU':'Gly', 'GGC':'Gly', 'GGA':'Gly', 'GGG':'Gly' 
}

def CodonsToProteins(ORF, genetic_code): 
    protein = ''
    for i in range ( 0, len(ORF), 3 ):
        codon = ORF(i: i+3)
        protein += genetic_code[codon]
    return protein
    

def mutate_seq(inputfile): 
    with open(inputfile, "r") as f: 
        seq = f.read() 
    seq = seq.replace("\n", "") 
    seq = seq.replace("\r", "") 
    return seq 
  
prt = mutate_seq("amino_acid.txt") 
dna = mutate_seq("DNA.txt") 
  
  
p = translate(dna[20:935]) 
p == prt  




 
