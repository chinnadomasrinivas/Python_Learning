number = int(input("enter the number :"))
divisoble = number % 5==0 and number%7==0
less_than = number <7
if divisoble or less_than:
    print(number)
else:
    print(number%5)
    print(number%7)