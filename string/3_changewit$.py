def change_first_char_occurrences(input_string):
   
    first_char = input_string[0]

   
    modified_string = first_char + input_string[1:].replace(first_char, '$')

    return modified_string

input_string = input("Enter a string: ")
modified_string = change_first_char_occurrences(input_string)
print("Modified string:", modified_string)
