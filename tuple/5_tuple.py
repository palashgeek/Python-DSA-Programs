my_tuple = (1,23,45,354,54,23,45)
my_list = []
for item in my_tuple:
    if my_tuple.count(item) > 1:
        if item not in my_list:
            my_list.append(item)
print(my_list)
