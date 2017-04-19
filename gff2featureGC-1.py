#! /usr/bin/env python3.6

#open and read the files
my_nts = open("/Users/ahchewning/desktop/programming/watermelon_files/watermelon.fsa")
my_genfeat = open("/Users/ahchewning/desktop/programming/watermelon_files/watermelon.gff")

#check the length of the DNA sequence
sequence = my_nts.read()
sequence_length = (len(sequence))
print (sequence_length)

#Calculate the G-C content in the entire sequence
G_count = sequence.count('G')
C_count = sequence.count('C')
GC_content = G_count + C_count
percent_GC = GC_content/ len(sequence)

#Declare a list for the sequence
nt_bases = []

#read each line of the fsa file into the list you just made
for line in sequence:
	line = line.strip('\n')
	nt_bases.append(line)

#count the number of start codons in the sequence

#isolate feature types. These are reported in field 3 of a gff. 

#close the files
my_nts.close()
my_genfeat.close()