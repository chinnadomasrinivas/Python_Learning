Units = int(input("Enter the Eletricity Bill :"))
Bill = 0
if Units >0 and Units <= 50 :
    Bill = Units*2
elif Units > 51 and Units <=150:
    Bill = 50*2 + (Units-50)*3
elif Units >151 and Units <= 250:
    Bill = 50*2 + 100*3 + (Units-150)*5
elif Units >= 251:
     Bill = 50*2 + 100*3 + 100*5 +(Units-250)*8
surcharge = Bill*0.2  
total_Bill = Bill + surcharge
print(total_Bill)           
    