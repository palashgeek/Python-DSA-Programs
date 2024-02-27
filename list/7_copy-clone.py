def remove_duplicates(input_list):
   
    return list(set(input_list))


input_list = input("Enter a list of elements separated by spaces: ").split()
unique_list = remove_duplicates(input_list)
print("List after removing duplicates:", unique_list)
