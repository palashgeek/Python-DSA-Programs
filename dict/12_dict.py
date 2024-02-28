'''

@Author: Palash Gupta

@Date: 2024-02-27 17:15:00

@Last Modified by: Palash gupta

@Last Modified time: 2024-02-27 17:15:00

@Title :Write a Python program to check multiple keys exists in a dictionary.
'''
def check_keys_exist(dictionary, keys):
    for key in keys:
        if key not in dictionary:
            return False
    return True

def main():
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

    keys_to_check = ['a', 'c', 'f']

    result = check_keys_exist(my_dict, keys_to_check)

    if result:
        print("All keys exist in the dictionary.")
    else:
        print("Not all keys exist in the dictionary.")

if __name__ == "__main__":
    main()
