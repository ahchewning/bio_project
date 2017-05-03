#! /usr/bin/env python3.6

#this script helps you determine the GC content
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


#print(gff + "\n" + genome)


#I want to calculate the GC content of different features in the watermelon genome
#First, I need to load the system module. Ask why.
import sys

genome = sys.argv[1]
gff    = sys.argv[2]

#Writing functions to clean up a DNA sequence
def clean_seq(input_seq):
	clean = input_seq.upper()
	clean = clean.replace('N','')
	return clean
	
	
def nuc_freq(sequence, base, sig_digs=2):
	#calculate the length of the sequence
	length = len(sequence)
	
	#count the number of this nucleotide
	count_of_base = sequence.count(base)
	
	#calculate the base of frequency
	freq_of_base = count_of_base/length
	
	#return the frequency and the length
	return (length, round(freq_of_base, sig_digs))
	
#make a dictionary key = gene name, value= another dictionary [key=exon number value= exon sequence]
#gene_sequence{cox1][1] = 'the sequence or the first exon of cox1'
#gene_sequence{cox1][2] = 'the sequence or the second exon of cox1'
#not usefule for anything but GC content
gene_sequences = {}



#get the gene name
#get the exon number(order is determined by the number in atributes feild
#make a dictionary 
genes
feature name
	key= gene neme
	value = sequence ['Exon number', v=seg]
	
exons, key =genename + Exon#




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
    if line_counter > 0:
        genome = genome + line

    # increment line_number: line number will increase by one in each loop
    line_counter += 1

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
    #line = line.rstrip('\n')

    types = line.split('type ')
    # print(other_type)
    
    #define your columns with split on each tab
    fields = line.split('\t')
    #declare that the 3rd column is the feature type
    type  = fields[2]
    #declare that colunm 4 holds the start site
    start = int(fields[3])
    #declare that column 5 holds the end site
    stop = int(fields[4])
    
    if (type == 'CDS'):   
    	#get the gene name
    	#print(fields[8])
   		attributes = fields[8].split(' ; ')
		#print(attrinutes[0])
    	gene_fields = atributes[0].slpit(' ')
    	gene_name = gene_fields[1])
    	#get the exon number
    	
    	if( 'exon' in gene_fields ):
    		exon_num =gene_fields[-1]
    		#exon_num = gene_feilds[3]
    		print("has exons: " + attriutes[0])
    		print(gene_name, exon_num)
    	#else:
    		#print ("Doesn't have exons: " + attributes[0])
    		
    		
    # print(type, "\t", start, "\t", end)
    
    #extract each feature from the genome remember: genome base it is 1 and python base is 0
    #still in your loop declare that fragments are between the start and end
    #this must be an integer (see above)
    fragment = genome[start-1:stop]
    fragment = clean_seq(fragment)
    
    if type in feature_sequence:
    	freature_sequences[type] += fragment
    else:
    	feature_sequence[type] =fragment
    	
    #determine the strand and rever complement or nah
    if(fields[6] =='-'):
    	fragment =reverse_comlement(fragment)
    
    	
    #store this sequence in the gene_sequence hash
    #do a has of hashes and try your best 
    
    
gff_in.close()

for feature, sequence in feature_sequnces.items():
	print(feature + "\t" + len(sequence))

#call your function to calculate the G + C
    
    

    #if type == 'CDS':
        #cds += fragment

    #elif type == 'intron':
        #intron += fragment

    #elif type == 'misc_feature':
       # misc += fragment

    #elif type == 'repeat_region':
        #repeats += fragment

    #elif type == 'rRNA':
        #rrna += fragment

    #elif type == 'tRNA':
        #trna += fragment
        	
	
#calculate the nucleotide composition of each feature
#loop over the 4 nucleotides

#declare a variabel list
types = ['cds', 'trna','rrna','intron','misc','repeats']

i=0

for feature_type in [cds, intron, misc, repeats, rrna, trna]:
	for nucleotide in ['A', 'C' , 'G', 'T']:
	
		(feature_length, feature_comp) = nuc_freq(feature_type, nucleotide, sig_digs=2)
		print(types[i] + "\t" + str(feature_length) + "\t" + str(feature_comp)+ "\t" + nucleotide)
		# print the output

	i = i + 1
		


# close the GFF file
gff_in.close()

#if on the _ use revers compliment and returen reverse compliment as fragment
#capture the gene name (the exon disagreement)
#fasta charate fasta header and then gene sequence
#parse 
we want the coding sequence for nad put together with out the intron
#read last plse 




