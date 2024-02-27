def lowercase_first_n_characters(input_string, n):
    return input_string[:n].lower() + input_string[n:]

input_string = input("Enter a string: ")
n = int(input("Enter the number of characters to lowercase: "))
lowercased_string = lowercase_first_n_characters(input_string, n)
print("String with first", n, "characters lowercased:", lowercased_string)
