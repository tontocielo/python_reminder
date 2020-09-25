#!usr/bin/env python3

#a modified fasta parser which stores a set of nested dictionaries with name of sequence, description, length, sequences and nt counts (Unhash print statement if needed). It also provides list of codons for each sequence in first ORF written to a file Python_08.codons-frame-1.nt.

import sys

file =open(sys.argv[1])
output = open('Python_08.codons-frame-1.nt', "w")

sequences = {}

for line in file:
  if line.startswith('>'):
    header = line.split()[0]
    id = header.lstrip('>') 
    description = line.split()[1:]    
    sequences[id] = {}
    sequences[id]['desc'] = description
    sequences[id]['seq'] = ''
    sequences[id]['len'] = 0
    sequences[id]['nt_comp'] = {}
    sequences[id]['nt_comp']['A'] = 0
    sequences[id]['nt_comp']['T'] = 0
    sequences[id]['nt_comp']['C'] = 0
    sequences[id]['nt_comp']['G'] = 0
  else:
    sequences[id]['seq'] +=  line.rstrip()
    sequences[id]['len'] += len(line.rstrip())
    sequences[id]['nt_comp']['A'] += line.count('A')
    sequences[id]['nt_comp']['T'] += line.count('T')
    sequences[id]['nt_comp']['G'] += line.count('G')
    sequences[id]['nt_comp']['C'] += line.count('C')

#print(sequences)

for seq in sequences:
  codons = []
  for i in range(0,sequences[seq]['len'],3): 
    codon = (sequences[seq]['seq'][i:i+3])
    if len(codon) == 3:
      codons.append(codon)
    else:
      next
  output.write(seq+'-frame1'+''\n'+sequences[seq]['seq']+'\n'+str(codons)+'\n')

print("List of codons for each sequences is written into file 'Python_08.codons-frame-1.nt'.")

file.close()
output.close()    


