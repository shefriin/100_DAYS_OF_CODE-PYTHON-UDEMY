SCORE = 0
def game(a,b,choice):
    global SCORE
    if (a["follower_count"] > b["follower_count"] and choice == "a") or (a["follower_count"] < b["follower_count"] and choice == "b"):
        SCORE += 1
        print("\n"*10)
        print(art14.logo)
        print(f"You're right! Current score: {SCORE}.")
        return False
    else:
        print(f"Sorry, that's wrong. Final score: {SCORE}")
        return True

import art14
print(art14.logo)
import random
from data14 import data
a = random.choice(data)
game_ended = False
while not game_ended:
    print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}")
    print(art14.vs)
    b = random.choice(data)
    while a == b:
        b = random.choice(data)
    print(f"Compare B: {b["name"]}, a {b["description"]}, from {b["country"]}")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    game_ended = game(a,b,choice)
    a = b
