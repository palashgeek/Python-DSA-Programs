'''

@Author: Palash Gupta

@Date: 2024-02-27 17:15:00

@Last Modified by: Palash gupta

@Last Modified time: 2024-02-27 17:15:00

@Title :Write a Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''

def generate_squares(n):
    dic = {}
    for i in range(1, n+1):
        dic[i] = i * i
    return dic

n = int(input("Enter a number:"))
Square_dict = generate_squares(n)
print(Square_dict)


