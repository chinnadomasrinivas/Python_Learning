word_1 = input("Enter the first string: ")
word_2 = input("Enter the second string: ")
length_1 = len(word_1)
length_2 = len(word_2)
result = word_1[length_1-length_2:] == word_2[0:]
print(result)