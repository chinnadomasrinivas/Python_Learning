num_1 = int(input(" enter the num_1 :"))
num_2 = int(input("Enter the num_2 :"))
condition_1 = num_1 == 6 or num_2 == 6
condition_2 = num_1 + num_2 == 6
condition_3 = num_1 - num_2 or num_2 - num_1 == 6
if condition_1 or condition_2 or condition_3:
     print("Lucky")
else:
    print("Not Lucky")