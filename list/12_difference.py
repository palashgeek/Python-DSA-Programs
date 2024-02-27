def get_list_difference(list1, list2):

    set1 = set(list1)
    set2 = set(list2)

    difference = set1 - set2

   
    difference_list = list(difference)
    return difference_list

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
difference = get_list_difference(list1, list2)
print("Difference between the two lists:", difference)
