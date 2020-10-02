#usr/bin/env python3

def gc_cont(dna):
  dna = dna.upper()
  Gs = dna.count('G')
  Cs = dna.count('C')
  gc_content = (Gs+Cs)*100/len(dna)
  return round(gc_content,2)

string = 'agTTGACAATGGAGAAAAAAAAAAAACCCCAcccA'

print(str(gc_cont(string))+'%')
