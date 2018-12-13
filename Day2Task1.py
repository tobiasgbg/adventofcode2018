#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
 
def main():
	cwd = os.getcwd()
 
	f = open(cwd + '/testfile.txt', 'r')
	#file_list = f.split()
 
	#with open (cwd + "/testfile.txt", "r") as myfile:
	#	file_list=myfile.readlines()
 
	two_counts = 0
	three_counts = 0
	
	alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	
	#file_list.append('')
 		
	for line in f:
		two_count_found = False
		three_count_found = False
	
		for alphabet in alphabet_list:
			if line.count(alphabet) == 3 and not three_count_found:
				three_counts += 1
				three_count_found = True
			elif line.count(alphabet) == 2 and not two_count_found:
				two_counts += 1
				two_count_found = True
			
	checksum = two_counts * three_counts

	print("Checksum is: " + str(checksum))
 
if __name__ == "__main__":
	main()