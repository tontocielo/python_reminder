#!/usr/bin/env python3

#this script takes a fasta/multifasta file from the command line and prints it to the output in specific window (width specified from command line)
import sys

input = open(sys.argv[1],"r")
width = int(sys.argv[2])

sequences = {}

for line in input:
  if line.startswith('>'):
    id = line
    sequences[id] = ''
  else:
    sequences[id] +=  line.rstrip()

for seq in sorted(sequences):
  print(seq.rstrip())
  for i in range(0,len(sequences[seq]),width):
    print(sequences[seq][i:i+width])



