import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

num = -1
if level == "easy":
    num = 10
elif level == "hard":
    num = 5

number = random.randint(1,100)

def guessing(user_no):
    if number < user_no :
        return 1
    elif number > user_no :
        return 0
    else:
        return -1

# flag = 1
for i in range(num,0,-1):
    print(f"You have {i} attempts remaining to guess the number.")
    guess = 544
    answer = guessing(guess)
    if answer == -1:
        print(f"You got it! The answer was {guess}.")
        # flag = 0
        break
    elif i == 1:
        print("YOU RAN OUT OF GUESSES. YOU LOST!")
    elif answer == 1:
        print("Too High.")
    elif answer == 0:
        print("Too Low.")

# if flag == 1:
#     print("YOU RAN OUT OF GUESSES. YOU LOST!")