'''

@Author: Palash Gupta

@Date: 2024-02-27 17:15:00

@Last Modified by: Palash gupta

@Last Modified time: 2024-02-27 17:15:00

@Title :Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
'''
initial_string = 'w3resource'

char_count = {}

for char in initial_string:
    if char in char_count:
        char_count[char] +=1
    else:
        char_count[char] = 1
print(char_count)

"""ask the slice way the list way after slicing the string .slice()"""
