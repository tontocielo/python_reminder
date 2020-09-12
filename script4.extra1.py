#!/usr/bin/env python3

#this script shuffles the sequence provided in the seq and seq_initial sections (they must be identical)

import random

seq = 'ACTGTTACGTAAT'
seq_initial='ACTGTTACGTAAT'

for i in range(len(seq)):
  A = random.randrange(len(seq))
  B = random.randrange(len(seq))
  a=seq[A]
  b=seq[B]
#  print(A,B,a,b)
  if a == b or A==B:
    continue
  if A<B:  
    seq=seq[:A]+b+seq[A+1:B]+a+seq[B+1:len(seq)]
#    print(seq)
  else:
    seq=seq[:B]+a+seq[B+1:A]+b+seq[A+1:len(seq)]
#    print(seq)
print('Initial sequence:','\t',seq_initial)
print('Shuffled sequence:','\t',seq)

