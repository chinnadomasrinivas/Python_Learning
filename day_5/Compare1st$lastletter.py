word = input("Enter a word: ")
length = len(word)
result = word[0] != word[length - 1]
print(result)