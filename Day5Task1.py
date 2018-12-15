import os
import sys
import re

def isReactive(a, b):
    if a.upper() == b.upper():
        if a.isupper() and b.islower():
             return True
        elif a.islower() and b.isupper():
            return True
        else:
            return False
    else:
        return False

def main():
    cwd = os.getcwd()
 
    with open (cwd + "/day5input.txt", "r") as myfile:
        file_list=myfile.readlines()

    str_list = ''.join(file_list).replace('\n', '')

    list_char = list(str_list)

    i = 0
    Stop = False
    is_reactive = True

    while(Stop == False):
        if isReactive(list_char[i], list_char[i+1]):
            list_char.pop(i)
            list_char.pop(i)
            is_reactive = True

        if i >= len(list_char) - 2 and is_reactive == False:
            Stop = True
        elif i >= len(list_char) - 2:
            i = 0
            is_reactive = False
        else:
            i += 1

    print(len(list_char))    

if __name__ == "__main__":
	main()