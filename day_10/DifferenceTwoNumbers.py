number_1 = int(input("enter the first number :"))
number_2 = int(input("enter the second number :"))
number_3 = int(input("enter the third number :"))
if number_1 - number_2 <25 and number_2 - number_3 <25 and number_3 - number_1 <25:
    print("Difference is less than 25")
else:
    print("Difference is not lees than 25")
