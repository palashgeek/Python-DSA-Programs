def sum_list_items(input_list):
    return sum(input_list)

input_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
total_sum = sum_list_items(input_list)
print("Sum of all items in the list:", total_sum)
