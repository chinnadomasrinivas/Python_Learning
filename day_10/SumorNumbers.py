A_number = int(input("Enter the A_number :"))
B_number = int(input("Enter the B_number :"))
condition_1 = A_number <20 or B_number <20
Sum = A_number + B_number 
condition_2 = Sum > 30 and Sum < 50
if condition_1 or condition_2:
    print(Sum)
else:
    print(A_number)
    print(B_number)
