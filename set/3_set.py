'''

@Author: Author Name

@Date: 2021-02-11 18:00:30

@Last Modified by: Author Name

@Last Modified time: 2021-02-11 18:00:30

@Title : remove a member to set.
'''

my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
my_set.discard(6) #error nai dega if element is not present
print("Updated Set:", my_set)
