def count_list_items(dictionary):
    count = 0
    for value in dictionary.values():
        if isinstance(value, list):
            #isinstance :isinstance(object, classinfo)

            count += len(value)
    return count

def main():
    my_dict = {'a': [1, 2, 3], 'b': 2, 'c': [4, 5], 'd': 'hello', 'e': [6]}

    list_items_count = count_list_items(my_dict)

    print("Number of items in list values:", list_items_count)

if __name__ == "__main__":
    main()
