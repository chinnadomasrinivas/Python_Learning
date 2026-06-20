word = input("enter word")
if word[0:3] == "NXT" and int(word[3 :]) % 2 ==0 or int(word[3 :] % 7==0):
    print("Special string")
else :
    print("Not a special string")