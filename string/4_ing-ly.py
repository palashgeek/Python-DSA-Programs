def add_ing_or_ly(input_string):
    if len(input_string) < 3:
        return input_string
    elif input_string.endswith("ing"):
        return input_string + "ly"
    else:
        return input_string + "ing"

input_string = input("Enter a string: ")
modified_string = add_ing_or_ly(input_string)
print("Modified string:", modified_string)