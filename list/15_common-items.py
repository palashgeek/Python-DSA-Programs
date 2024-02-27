def find_common_items(list1, list2):
    common_items = []
    for item in list1:
        if item in list2:
            common_items.append(item)
    return common_items


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_items = find_common_items(list1, list2)
print("Common items from the two lists:", common_items)
