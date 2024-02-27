def remove_duplicates_from_list_of_lists(list_of_lists):
    unique_lists = []
    for inner_list in list_of_lists:
        if inner_list not in unique_lists:
            unique_lists.append(inner_list)
    return unique_lists

list_of_lists = [[1, 2, 3], [4, 5, 6], [1, 2, 3], [7, 8, 9], [4, 5, 6]]
unique_lists = remove_duplicates_from_list_of_lists(list_of_lists)
print("List of lists after removing duplicates:", unique_lists)
