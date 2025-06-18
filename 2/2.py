print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10,12, or 15? "))
num = int(input("How many people to split the bill? "))
pay = (total + (total*tip/100) ) / num
pay = round(pay,2)
# print("Each person should pay: $"+str(pay))
print(f"Each person should pay: ${pay}")