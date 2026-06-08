number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
result_1 = number_1 <= number_2
result_2 = number_2 <= number_1
print("A <= B is "+str(result_1))
print("B <= A is "+str(result_2))