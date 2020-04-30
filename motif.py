#!/usr/bin/env python3

#gaining access to regular expression module
import re

#set variable equal to kmer 
sixmer = "TGGCGA"

#open file with sequence to read it , set handle
with open ("og_seq.fasta", "r") as in_handle:
	
#interpret handle and set interpretation to variable
	sequence = in_handle.read()

#turn variable holding read file into a collection of strings
seq = str(sequence)

#break string at desired kmer, creating a list and save as variable
seq_list = sequence.split(sixmer)

#print list of split strings
#print(seq_list)

#take first item in list of split strings, out of the list
seq_list.remove(seq_list[0])

#print list of split strings (sans first item)
#print(seq_list)

#create function that takes in two parameters #the two parameters take in two different collections
#sort list of split strings without the first item
def prepend(list, str):

	str += "{0}"

#break string at desired kmer, creating a list and save as variable
#store an item from the list in a string that as changing each iteration
	list = [str.format(i) for i in list]


#retreive list from function
	return (list)

#call function with parameters list of split strings and kmer variable
#assign output from function to variable 
repeat_list = prepend(seq_list, sixmer)

#create lists to short repeats into
sorted_long = []
sorted_medium = []
sorted_short= []

#iterate through function output and sort into corresponsing list based on length
for item in repeat_list:
	if(len(item) == 255):
		sorted_long.append(item)
	elif(len(item) == 205):
		sorted_medium.append(item)
	else:
		sorted_short.append(item)

#print sorted lists
print(sorted_long)
print(sorted_medium)
print(sorted_short)

print(len(sorted_long))
print(len(sorted_medium))
print(len(sorted_short))
#print interation of function output
#	print(item)
