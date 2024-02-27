def multiply_list_items(input_list):
    result = 1
    for item in input_list:
        result *= item
    return result

input_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
product = multiply_list_items(input_list)
print("Product of all items in the list:", product)
