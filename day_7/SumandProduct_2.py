number_1 = int(input("Enter the first number:"))
number_2 = int(input("Enter the second number"))
condition_1 = (number_1 + number_2) < 0
condition_2 = (number_1 *  number_2) < 0
result = condition_1 or condition_2
print(result)