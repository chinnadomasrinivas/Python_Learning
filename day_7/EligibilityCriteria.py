M = int(input("Enter the maths marks :"))
P = int(input("Enter the physics marks :"))
C = int(input("Enter the chemistry marks :"))
condition_1 = M >= 70 and P >= 60 and C >= 60
condition_2 = M + P + C >=180
result = (condition_1 or condition_2)
print(result)
