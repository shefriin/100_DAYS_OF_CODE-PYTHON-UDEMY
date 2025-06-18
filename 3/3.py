'''
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra = input("do you want extra cheese? Y or N: ")
bill = 0
if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill+=2
elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill+=3
elif size == "L":
    bill+= 25
    if pepperoni == "Y":
        bill+=3
else:
    print("Typed Wrong")
if extra == "Y":
    bill+=1
print(f"Your final bill is: ${bill}")
'''
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
direction = input("You are at a crossroad. Do you wanna go left or right? ")
if direction.lower() == "left":
    lake = input('You see a lake. Do you wanna "swim" or "wait?" ')
    if lake.lower() == "wait":
        print("You have successfully crossed the lake.")
        door = input("There are 3 doors. Choose the \"red\", \"blue\" or \"yellow\" door: ")
        if door.lower() == "yellow":
            print("YOU FOUND THE TREASURE! YOU WIN.")
        elif door.lower() == "red":
            print("Room is in fire. You lost.")
        elif door.lower() == "blue":
            print("Room is flooded. You lost.")
        else:
            print("Invalid colour entered.")
    elif lake.lower() == "swim":
        print("There was a Shark! You lost.")
    else:
        print("Invalid choice entered.")
else:
    print("A car hit you! You lost.")