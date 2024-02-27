def are_circularly_identical(list1, list2):

    if len(list1) != len(list2):
        return False

    for i in range(len(list1)):
        if list1[i:] + list1[:i] == list2:
            return True

    return False


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 1, 2]
list3 = [4, 5, 6, 7, 8]
print("Are list1 and list2 circularly identical?", are_circularly_identical(list1, list2))
print("Are list1 and list3 circularly identical?", are_circularly_identical(list1, list3))
