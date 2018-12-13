#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
 
def main():
	cwd = os.getcwd()
 
	f = open(cwd + '/testfile.txt', 'r')
 
	frequency = 0
 
	for line in f:
		if '+' in line:
			frequency = frequency + int(line.replace('+',''))
		elif '-' in line:
			frequency = frequency - int(line.replace('-',''))
		else:
			print("Falsely parsed line " + line)

	print("Final frequency is: " + str(frequency))
 
if __name__ == "__main__":
	main()