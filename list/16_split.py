def split_list_based_on_first_character(word_list):
   groups = {}
   for word in word_list:
      first_char = word[0]

      if first_char in groups:
            groups[first_char].append(word)
      else:
          groups[first_char] = [word]

   return groups


word_list = ['apple', 'banana', 'ant', 'ball', 'cat', 'car', 'dog']
grouped_words = split_list_based_on_first_character(word_list)
print("List split based on first character of word:")
for first_char, words in grouped_words.items():
    print(f"{first_char}: {words}")
