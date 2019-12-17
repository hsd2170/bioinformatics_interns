##!/usr/bin/env python3
import argparse 
import FileIO
import Random
import OS
import numpy as np

#parser = argparse.ArgumentParser(description = 'State header')
#parser.add_argument("-header", required)
#args = parser.parse_args()

nuc_list= ["A","T","C","G"] #creates a list of nucs to use in our function

def repeat_seq(length): # creating the function that will create the repeats
    your_letters='ATCG' #list of characters to use in function
    return ''.join((random.choice(your_letters) for i in range(length)) #generating the random list of nucs to use for repeats

repeat_seq1= repeat_seq(30) #generating the random lists of nucs that are 30 base pairs in length
repeat_seq2=repeat_seq(30)
repeat_seq3 =repeat_seq(30)
repeat_seq4 = repeat_seq(30)
repeat_seq5 = repeat_seq(30)

def new_fasta(): #making the fasta creation function

 #trying to see if this works and if it doesn't, pring the error message
	try:
		with open("psuedo_protein.fasta",w) as in_handle: #opens the file and write the repeats in it
			in_handle.write(repeat_seq1, repeat_seq2, repeat_seq3, repeat_seq4, repeat_seq5)


	except as IOError:
	#this is the exception error that will help the code
#		print("IOError")

	
