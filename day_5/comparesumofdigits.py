number = input("Enter a number: ")
first_digit = int(number[0])
last_digit = int(number[-1])
sum_of_digits = first_digit + last_digit
result = sum_of_digits > 7
print(result)