A = int(input(" enter 1st side of triangle :"))
B = int(input("enter the 2nd side of triangle :"))
C = int(input("enter the 3rd side of triangle :"))
if A + B > C and B + C > A and C + A > B :
    print("its a Triangle")
else:
    print(" ita not a triangle")