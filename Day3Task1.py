import os
import sys
 
def main():
	cwd = os.getcwd()
 
	#f = open(cwd + '/testfile.txt', 'r')
	#file_list = f.split()
 
	with open (cwd + "/testfile.txt", "r") as myfile:
		file_list=myfile.readlines()
	#file_list.append('')

	square = [[0 for x in range(1000)] for y in range(1000)] 
	overlap = 0

	for line in file_list:
		line_split = line.split('@')
		line_split = line_split[1]
		line_split = line_split.split(',')
		x_start = line_split[0]
		line_split = line_split[1].split(':')
		y_start = line_split[0]
		line_split = line_split[1].split('x')
		x_length = line_split[0]
		y_length = line_split[1]

		for i in range(0, int(x_length)):
			for j in range(0, int(y_length)):
				square[int(x_start)+i][int(y_start)+j] += 1

	for i in range(0, len(square[0])):
		for j in range(0, len(square)):
			if square[i][j] > 1:
				overlap += 1

	#print("x: " + x_start + " y: " + y_start + " x size: " + x_length + " y size: " + y_length)
	print("Overlap is: " + str(overlap))

if __name__ == "__main__":
	main()