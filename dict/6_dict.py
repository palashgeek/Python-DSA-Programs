'''

@Author: Palash Gupta

@Date: 2024-02-27 17:15:00

@Last Modified by: Palash gupta

@Last Modified time: 2024-02-27 17:15:00

@Title :Write a Python program to remove a key from a dictionary.
'''

my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

key_to_remove = 'age'
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print(f"Key '{key_to_remove}' removed using del:", my_dict)
else:
    print(f"Key '{key_to_remove}' not found in the dictionary.")


key_to_remove = 'city'
removed_value = my_dict.pop(key_to_remove, None)
if removed_value is not None:
    print(f"Key '{key_to_remove}' removed using pop:", my_dict)
else:
    print(f"Key '{key_to_remove}' not found in the dictionary.")

