#!usr/bin/env python3

#a modified fasta parser which stores a set of nested dictionaries with name of sequence, description, length, sequences and nt counts (Unhash print statement if needed). It also provides list of codons for each sequence in all ORFs written to a file Python_08.codons-frame-6.nt and corresponding aa sequence

import sys

file =open(sys.argv[1])
output = open('Python_08.codons-frame-6.nt', "w")

translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}

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
  rev=sequences[seq]['seq'][::-1]
  rev_com = rev.replace('A','t').replace('T','a').replace('G','c').replace('C','g')
  rev_comp = rev_com.upper()
  for frame in range(0,6):
    if frame < 3:
      codons = []
      start_nt = frame
      for i in range(start_nt,sequences[seq]['len'],3): 
        codon = (sequences[seq]['seq'][i:i+3])
        if len(codon) == 3:
          codons.append(codon)
        else:
          next
      output.write(seq+'-frame'+str(frame+1)+'\n'+sequences[seq]['seq']+'\n'+str(codons)+'\n')
      aa_seq = ''
      for cod in codons:
        aa_seq += translation_table[cod] 
      output.write(aa_seq+'\n'+'\n')
    elif frame == 3:
      codons = []
      start_nt = 0
      for i in range(start_nt,sequences[seq]['len'],3): 
        codon = rev_comp[i:i+3]
        if len(codon) == 3:
          codons.append(codon)
        else:
          next
      output.write(seq+'-frame'+str(frame+1)+'\n'+sequences[seq]['seq']+'\n'+str(codons)+'\n')
      aa_seq = ''
      for cod in codons:
        aa_seq += translation_table[cod] 
      output.write(aa_seq+'\n'+'\n')
    elif frame == 4:
      codons = []
      start_nt = 1
      for i in range(start_nt,sequences[seq]['len'],3): 
        codon = rev_comp[i:i+3]
        if len(codon) == 3:
          codons.append(codon)
        else:
          next
      output.write(seq+'-frame'+str(frame+1)+'\n'+sequences[seq]['seq']+'\n'+str(codons)+'\n')
      aa_seq = ''
      for cod in codons:
        aa_seq += translation_table[cod] 
      output.write(aa_seq+'\n'+'\n')
    else:
      codons = []
      start_nt = 2
      for i in range(start_nt,sequences[seq]['len'],3): 
        codon = rev_comp[i:i+3]
        if len(codon) == 3:
          codons.append(codon)
        else:
          next
      output.write(seq+'-frame'+str(frame+1)+'\n'+sequences[seq]['seq']+'\n'+str(codons)+'\n')
      aa_seq = ''
      for cod in codons:
        aa_seq += translation_table[cod] 
      output.write(aa_seq+'\n'+'\n')

print("List of codons for each sequences is written into file 'Python_08.codons-frame-6.nt'.")

file.close()
output.close()    


