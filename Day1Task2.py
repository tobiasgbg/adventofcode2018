#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
 
def main():
	cwd = os.getcwd()
 
	#f = open(cwd + '/testfile.txt', 'r')
	#file_list = f.split()
 
	with open (cwd + "/testfile.txt", "r") as myfile:
		file_list=myfile.readlines()
 
	frequency = 0
	all_frequencies = []
	
	file_list.append('')
 
	i = 0
	stop = False
 
	while(stop == False):
	
		if file_list[i] != '':
			if '+' in file_list[i]:
				frequency = frequency + int(file_list[i].replace('+',''))
			elif '-' in file_list[i]:
				frequency = frequency - int(file_list[i].replace('-',''))
			else:
				print("Falsely parsed line " + file_list[i])
			print("Current frequency: " + str(frequency))
			
			i += 1
		else:
			i = 0
		
		for element in all_frequencies:
			if element == frequency:
				stop = True

		if file_list[i] != '':
			all_frequencies.append(frequency)
	

	print("Final frequency is: " + str(frequency))
 
if __name__ == "__main__":
	main()