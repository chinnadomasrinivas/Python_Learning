N = int(input(" Enter the number :"))
str_N = str(N)
if (N % 9 == 0) or (int(str_N[0])==9 or int(str_N[1]) == 9):
    print("Lucky number")
else :
    print("unlucky number")