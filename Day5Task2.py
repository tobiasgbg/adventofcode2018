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

    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_dict = {}

    for alphabet in alphabet_list:
        i = 0
        is_reactive = True
        Stop = False

        new_str = str_list.replace(alphabet, '')
        new_str = new_str.replace(alphabet.upper(), '')

        new_list = list(new_str)

        while(Stop == False):
            if isReactive(new_list[i], new_list[i+1]):
                new_list.pop(i)
                new_list.pop(i)
                is_reactive = True

            if i >= len(new_list) - 2 and is_reactive == False:
                alphabet_dict[alphabet] = len(new_list)
                Stop = True
            elif i >= len(new_list) - 2:
                i = 0
                is_reactive = False
            else:
                i += 1

    print(alphabet_dict)

    smallest_string_nr = 100000
    best_char = ''

    for alphabet in alphabet_dict:
        if alphabet_dict.get(alphabet) < smallest_string_nr:
            smallest_string_nr = alphabet_dict.get(alphabet)
            best_char = alphabet

    print("Best char: " + best_char + " String length: " + str(smallest_string_nr))

if __name__ == "__main__":
	main()