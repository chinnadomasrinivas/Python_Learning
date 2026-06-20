num = int(input("Enter the num :"))
Not_divisoble = (num%2 != 0) and (num%3 != 0) and (num%5 != 0) and (num%7 != 0)
if Not_divisoble:
    print("True")
else:
    print("False")