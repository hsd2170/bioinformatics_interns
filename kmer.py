#!/usr/bin/env python3
#import modules
from collections import Counter
from collections import OrderedDict

#create function that takes two parameters
#create a list that searches for sets of similar nucleotides by "stepping" through a sequence and recording each of parameter length with corresponding base
def get_all_k_mer(string, k=1):
#find the length of the sequence
   length = len(string)
#obtain list output from function   
	return [string[i: i+ k] for i in range(length-k+1)]

#open a file to read, replace linefeed with space
with open ("/Users/nhenhunter/rosalind/og_seq.fasta", "r") as in_handle:
	string = in_handle.read().replace('\n', '')

print(string)
#call function and provide string and kmer length as parameters
#create a dictionary using a module
kmer_dict = Counter(get_all_k_mer(string, k=6))

#print dictionary
print(kmer_dict)




#obtain list output from function
 





