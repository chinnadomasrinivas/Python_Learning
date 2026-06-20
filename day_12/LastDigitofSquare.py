N = input()
l_N = len(N)
Square = str(int(N)**2)
l_square = len(Square)
if (int(N[l_N-1]) == int(Square[l_square-1])):
    print("Equal")
else:
    print("Not Equal")
