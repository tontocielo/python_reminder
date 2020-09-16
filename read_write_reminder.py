#!usr/bin/env python3

#1st way
#file = open("seq.nt.fa")
#contents=file.read()
#print(contents)
#file.close()

#2nd way
file=open("seq.nt.fa")
for line in file:
	print(line.rstrip()) #rstrip removes newline sign

file.close()

#3rd way

with open("seq.nt.fa") as file2, open('file_output2','w') as output:
	for line in file2:
		line2 = line
		output.write(line2)

print("Wrote to file 'file_output2'") 
