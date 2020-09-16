#!usr/bin/env python3

my_dict = {}

file = open('Python_06.seq.txt','r')
for line in file:
  line = line.rstrip()
  id, seq = line.split() 
  my_dict[id]={}
  nts = set(seq)
  for nt in nts:
    number = seq.count(nt)
    my_dict[id][nt]=number 
  print(id,my_dict[id],'GC content:', round(((my_dict[id]['G']+my_dict[id]['C'])*100/len(seq)),2))


file.close()
