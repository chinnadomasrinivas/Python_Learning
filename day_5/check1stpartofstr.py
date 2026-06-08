S1 = input("Enter the first string: ")
S2 = input("Enter the second string: ")
L1 = len(S1)
L2 = len(S2)
result = S1[:L2] == S2[:]
print(result)