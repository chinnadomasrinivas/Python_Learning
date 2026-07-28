number = int(input("Enter the number :"))
counter = 1
while counter <= number:
    result = (str(counter) + " ") * counter
    print(result)
    counter = counter + 1 