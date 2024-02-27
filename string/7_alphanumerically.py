def print_sorted_unique_words(input_string):
   
    words = input_string.split(',')

   
    words = [word.strip() for word in words]

   
    unique_words = sorted(set(words))

   
    print("Unique words in sorted form:")
    for word in unique_words:
        print(word)

input_string = input("Enter a comma-separated sequence of words: ")
print_sorted_unique_words(input_string)
