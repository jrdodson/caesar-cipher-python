#! /usr/bin/python
#  John Ryan Dodson 2/6/2014

import sys
import string

alpha = []

def generateAlphabet():
    for item in range(97,123):
        alpha.append(chr(item))


#go through each item in the string
#if it's a character, perform a shift and append
#otherwise it's numeric or punctuation, so just append
def decrypt(shift, cipher):
    result = ""
    for item in cipher:
        if item.isalpha():
            ch = (ord(item)-shift)%len(alpha)
            result+=alpha[ch]
        else:
            result+=item
    print  str(shift) + '\n\t'+ result

def main(argv):
	if (len(sys.argv) != 2):
		sys.exit('Usage: <program>.py <ciphertext file> or "ciphertext string"')

	#read in file contents
	ciphertext =""
	try:
		with open(sys.argv[1], 'rw') as infile:
			for line in infile:
				ciphertext+=line
		infile.close()
	except IOError:
		ciphertext=sys.argv[1] #assume we get a string if we don't get a file

	#generate alphabet and decrypt
	generateAlphabet()
	index = 0
	while index!=len(alpha):
		decrypt(index, ciphertext.lower()) #just for fun, we'll keep it lowercase
		index+=1

if __name__ == "__main__":
    main(sys.argv[1:])
