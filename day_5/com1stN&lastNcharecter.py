word = input("Enter a word: "       )
L = len(word)
num = int(input("Enter the number of characters to compare: "))
S = word[:num]
P = word[L-num:]
result  = S != P
print(result)