N = int(input("Enter the number of inputs:"))
count = 1 
sum = 0
while count <= N:
    n = int(input("Enter a number:"))
    sum = sum + n
    count = count + 1 
result = sum/N 
print(result)
    