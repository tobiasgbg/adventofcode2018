#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import sys
 
def compare(a,b):
	match = 0
	for i in range(0, len(a)-1):
		if a[i] == b[i]:
			match+=1
	
	if match == 25:
		print("These two lines matches almost: " + a + " " + b)
		print(str(match))
		return True
	else:
		return False
 
def main():
	cwd = os.getcwd()
 
	#f = open(cwd + '/testfile.txt', 'r')
	#file_list = f.split()
 
	with open (cwd + "/testfile.txt", "r") as myfile:
		file_list=myfile.readlines()
	#file_list.append('')
		
	for i in range(0, len(file_list)):
		for j in range(0, len(file_list)):
			if i != j:
				if compare(file_list[i], file_list[j]) == True:
					print("These two lines matches almost: " + str(file_list[i]) + " " + str(file_list[j]))
					return

 
if __name__ == "__main__":
	main()