def find_smallest_number(input_list):
    return min(input_list)

input_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
smallest_number = find_smallest_number(input_list)
print("Smallest number in the list:", smallest_number)
