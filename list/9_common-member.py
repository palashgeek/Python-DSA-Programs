def has_common_member(list1, list2):
    set1 = set(list1)
    for item in list2:
        if item in set1:
            return True
    return False


list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
print("Do the lists have at least one common member?", has_common_member(list1, list2))
