#!usr/bin/env python3

import sys

file =open(sys.argv[1])

sequences = {}

for line in file:
  if line.startswith('>'):
    id = line.split()[0]
    sequences[id] = ''
  else:
    sequences[id] +=  line.rstrip()

#printing 1st  10 nt of the sequences + seq id
for seq in sorted(sequences):
  print(seq,'\t',sequences[seq][:10])

#calculating sequence lenght
#for seq in sequences:
#  print(seq,'\t', len(sequences[seq]))
