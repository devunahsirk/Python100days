print("Welcome to the tip calculator")
bill=float(input("What was the total bill? "))
tip=float(input("What percentage tip would you like to tip "))
number=float(input("How many people to split the bill? "))
bill=bill*(100+tip)/100
total=bill/number
print(round(total,2))
