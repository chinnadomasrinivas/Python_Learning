number_1 = int(input("Enter the first number:"))
number_2 = int(input("Enter the second num :"))
condition_1 = number_1 + number_2 < 10
condition_2 = number_1 - number_2 < 10
condition_3 = number_1 > 5 and number_1 < 30
result = condition_1 or condition_2 or condition_3
print(result)