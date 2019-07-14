#!/usr/bin/python3

import sys,re

dest_to_binary = {
	"null":"000",
	"M":"001",
	"D":"010",
	"MD":"011",
	"A":"100",
	"AM":"101",
	"AD":"110",
	"AMD":"111"
}

comp_to_binary = {
	"0" : {
	"0":"101010",
	"1":"111111",
	"-1":"111010",
	"D":"001100",
	"A":"110000",
	"!D":"001101",
	"!A":"110001",
	"-D":"001111",
	"-A":"110011",
	"D+1":"011111",
	"A+1":"110111",
	"D-1":"001110",
	"A-1":"110010",
	"D+A":"000010",
	"D-A":"010011",
	"A-D":"000111",
	"D&A":"000000",
	"D|A":"010101"
	},

	"1" : {
	"M":"110000",
	"!M":"110001",
	"-M":"110011",
	"M+1":"110111",
	"M-1":"110010",
	"D+M":"000010",
	"D-M":"010011",
	"M-D":"000111",
	"D&M":"000000",
	"D|M":"010101"
	}
}

jump_to_binary = {	
	"null":"000",
	"JGT":"001",
	"JEQ":"010",
	"JGE":"011",
	"JLT":"100",
	"JNE":"101",
	"JLE":"110",
	"JMP":"111"
}

def binary_rep(num):
	assert isinstance(num,int),"num is not int"

	s = ""
	for i in range(15):
		if num & (1 << i):
			s += "1"
		else:
			s += "0"

	return s[::-1]

def assemble(filename):

	opfile = open(filename.split(".asm")[0]+".hack", 'w')

	with open(filename, 'r') as file:

		for line in file:

			#ignore empty lines, indentations, line comments and inline comments
			line = line.split('//')[0].strip()
			
			if line:
				
				print("converting...",line)

				#handle C instr
				if line.startswith('@'):					
					opfile.write("0"+binary_rep(int(line[1:]))+"\n")

				#handle A inst
				else:

					equalindex = line.find("=")
					colonindex = line.find(";")

					if equalindex != -1:
						dest = line[:equalindex]
					else:
						dest = "null"

					if colonindex != -1:
						jump = line[colonindex+1:]						
					else:
						jump = "null"

					if equalindex!=-1 and colonindex!=-1:
						comp = line[equalindex+1:colonindex]
					elif equalindex != -1:
						comp = line[equalindex+1:]
					else:
						comp = line[:colonindex]


					abit = '1' if 'M' in comp else '0'

					try:
						destbits = dest_to_binary[dest]
						compbits = comp_to_binary[abit][comp]
						jumpbits = jump_to_binary[jump]
					except:
						print("assembling failed")
						sys.exit(1)
					
					result = "111" + abit + compbits + destbits + jumpbits
					
					opfile.write(result+"\n")

	opfile.close()

def main():
	args = sys.argv[1:]
	filename = args[0]
	assemble(filename)
	return

if __name__ == "__main__":
	main()