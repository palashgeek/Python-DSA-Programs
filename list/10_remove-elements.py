def remove_elements(input_list):
    indices_to_remove = [0, 4, 5]
    new_list = [input_list[i] for i in range(len(input_list)) if i not in indices_to_remove]
    return new_list


specified_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result_list = remove_elements(specified_list)
print("List after removing 0th, 4th, and 5th elements:", result_list)
