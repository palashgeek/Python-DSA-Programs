from copy import deepcopy
samtuple = ("gfhsdjf", 'J', 34, 32.234, [], True)
print(samtuple)

sampletuple = deepcopy(samtuple)
sampletuple[4].append(43)
print(sampletuple)
print(samtuple)
