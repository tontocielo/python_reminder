#!usr/bin/env python3

file = open('Python_06.seq.txt','r')
for line in file:
  line = line.rstrip()
  id, seq = line.split() 
  rc_line = seq.replace('A','t').replace('T','a').replace('G','c').replace('C','g')
  rc_line = rc_line.upper()
  rc_line=rc_line[::-1]
  print('>'+id,'reverse_complement','\n'+rc_line)
