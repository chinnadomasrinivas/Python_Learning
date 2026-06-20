N = int(input("Enter the years :"))
Years = (N//365)
print(Years)
remaining_days = N - Years*365
Weeks = remaining_days // 7
print(Weeks)
days = remaining_days - Weeks *7
print(days)
