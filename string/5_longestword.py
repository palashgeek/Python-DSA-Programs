def find_longest_word(words):
    longest_length = 0
    for word in words:
        if len(word) > longest_length:
            longest_length = len(word)
    return longest_length

word_list = ["apple", "banana", "orange", "kiwi", "pineapple"]
longest_length = find_longest_word(word_list)
print("Length of the longest word:", longest_length)