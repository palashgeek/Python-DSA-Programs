def count_substring_occurrences(input_string, substring):
    count = input_string.count(substring)
    return count

input_string = input("Enter a string: ")
substring = input("Enter a substring to count: ")
occurrences = count_substring_occurrences(input_string, substring)
print(f"Number of occurrences of '{substring}': {occurrences}")