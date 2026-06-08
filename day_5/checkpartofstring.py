word_1 = input()

word_2 = input()
L = len(word_2)
num = int(input())
index = word_1[num:num+L-1]
result  = word_2[0:] == word_1[num:num+L]
print(result)