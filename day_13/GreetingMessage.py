Time = int(input("Enter the time :"))
if Time >= 4 and Time < 12 :
    print("Good morning")
elif Time >= 12 and Time < 16 :
    print("Good Afternoon")
elif Time>= 16 and Time <20 :
    print("Good Evining")
elif Time >= 20 or Time < 4:
    print("Good Night")