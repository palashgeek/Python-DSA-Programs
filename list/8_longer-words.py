def find_words_longer_than_n(words, n):
    longer_words = [word for word in words if len(word) > n]
    return longer_words

input_list = input("Enter a list of words separated by spaces: ").split()
n = int(input("Enter the minimum length for words: "))
longer_words_list = find_words_longer_than_n(input_list, n)
print("Words longer than", n, "characters:", longer_words_list)

