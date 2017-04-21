#! /usr/bin/env python3.6

#Hard coding is unreasonable if you will reuse your code. Ask for help about this.
#the fist element is the name of your script
#sys.arg of 0 is the name or path to your script as you called
#./argv.py 1 pam zach nail youg and so on 
#looped over all of them and stored them in order in our log v array
#you can use this with argument in your program to keep arguments in order. 
#now you have a way to caputre file names 

#usage = sys.argv[0] + ": genome.fasta features.gff"

#if len(sys.argv) < 3:
    #print(usage)
    #sys.exit("\nThis script requires both a FASTA file and a GFF file\n")

genome = sys.argv[1]
gff    = sys.argv[2]

print(gff + "\n" + genome)
#I want to calculate the GC content of different features in the watermelon genome

#First, I need to load the system module. Ask why.
import sys

#declare the the file (one is a sequence and one is a gff) 
gff_file = 'watermelon.gff'
fsa_file = 'watermelon.fsa'

# Open the files for reading and call it '_in' This is how you get to the content.
gff_in = open(gff_file, 'r')
fsa_in = open(fsa_file, 'r')

# declare and empty variable. It will hold the content of gff_file (aka the sequence)
genome = ''

#initialize line counter starting at line zero
line_counter = 0

# read in the genome file contents line by line in a for loop
for line in fsa_in:
    # print(str(line_number) + ": " + line)

    # Use rstrip to remove newline's by declaring the newline character in rstrip
    line = line.rstrip('\n')

    #Ask Andy to explain this later
    if line_number > 0:
        genome = genome + line

    # increment line_number: line number will increase by one in each loop
    line_number += 1

# Ask if you got captured the lines who you wanted?
# print(len(genome))
    
# Remember to close the file 
fsa_in.close()

#Declare empty variables for each feature type

cds     = ''
trna    = ''
rrna    = ''
intron  = ''
misc    = ''
repeats = ''

# read in the GFF file remember this is tab delimited and each column hold different info(google)
for line in gff_in:

    # remove newline's - could also use strip
    line = line.rstrip('\n')

    types = line.split('; type ')
    other_type = types[len(types)-1]
    # print(other_type)
    
    #define your columns with split on each tab
    fields = line.split('\t')
    #declare that the 3rd column is the feature type
    type  = fields[2]
    #declare that colunm 4 holds the start site
    start = int(fields[3])
    #declare that column 5 holds the end site
    end   = int(fields[4])
    
    # print(type, "\t", start, "\t", end)

    # extract each feature from the genome remember: genome base it is 1 and python base is 0
    #still in your loop declare that fragments are between the srart and end
    #this must be an integer (see above)
    fragment = genome[start-1:end]

    if type == 'CDS':
        cds += fragment

    if type == 'intron':
        intron += fragment

    if type == 'misc_feature':
        misc += fragment

    if type == 'repeat_region':
        repeats += fragment

    if type == 'rRNA':
        rrna += fragment

    if type == 'tRNA':
        trna += fragment

# print the output
print(cds.count('G'))
print(cds.count('C'))
    

# close the GFF file
gff_in.close()


#Before class
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

