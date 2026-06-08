length = int(input("Enter the length: " ))
breadth = int(input("Enter the breadth: "))
Area = length*breadth
perimeter = 2*(length+breadth)
result = Area <= perimeter
print(result)