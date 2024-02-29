'''
@Author: Author Name

@Date: 2021-02-11 18:00:30

@Last Modified by: Author Name

@Last Modified time: 2021-02-11 18:00:30

@Title : Frozwen set
'''


'''The frozenset() function returns an unchangeable frozenset object (which is like a set object, only unchangeable).'''

mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
x[1] = "strawberry"