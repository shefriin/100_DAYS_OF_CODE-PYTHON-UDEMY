''' #STEP 1
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("Guess a letter: \n")
guess.lower()
for i in chosen_word:
    if i == guess:
        print("Right")
    else:
        print("Wrong")
'''
''' #STEP 2
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)
guess = input("Guess a letter: \n")
guess = guess.lower()
display = ""
for i in chosen_word:
    if i == guess:
        display += i
    else:
        display += "_"
print(display)
'''
''' #STEP 3
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)
list1 = []
game_over = False
while not game_over:
    guess = input("Guess a letter: \n")
    guess = guess.lower()
    display = ""
    for i in chosen_word:
        if i == guess:
            display+= guess
            list1.append(guess)
        elif i in list1:
            display += i
        else:
            display += "_"
    print(display)
    if "_" not in display:
        print("You win")
        game_over = True
print(list1)
'''
''' #STEP 5
stages = [
    """
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =======""",
    
    """
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =======""",

    """
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =======""",

    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =======""",

    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =======""",

    """
     +---+
     |   |
     O   |
         |
         |
         |
    =======""",

    """
     +---+
     |   |
         |
         |
         |
         |
    ======="""
]

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)
list1 = []
game_over = False
lives = 6
while not game_over:
    guess = input("Guess a letter: \n")
    guess = guess.lower()
    display = ""

    for i in chosen_word:
        if i == guess:
            display+= guess
            list1.append(guess)
        elif i in list1:
            display += i
        else:
            display += "_"
    print(display)
    if "_" not in display:
        print("You win!")
        game_over = True
    
    if guess not in chosen_word:
        lives -= 1
    print(stages[lives])
    if lives == 0:
        print("You Loose!")
        game_over = True
'''
import hangman_words
import hangman_art
import random
print(hangman_art.logo)
stages = hangman_art.hangman_stages
word_list = hangman_words.hangman_wordlist
chosen_word = random.choice(word_list)
# print(chosen_word)
placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print("Word to guess: "+placeholder)
list1 = []
game_over = False
lives = 6
while not game_over:
    guess = input("Guess a letter: ")
    guess = guess.lower()
    print(f"*****************{lives}/6 left*********************")
    
    display = ""

    if guess in list1:
        print("You've already guess the letter: "+guess+"\n")
        continue

    for i in chosen_word:
        if i == guess:
            display+= guess
            list1.append(guess)
        elif i in list1:
            display += i
        else:
            display += "_"

    print(display)
    
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed: {guess}, that's not in the word.\nYou lose a life.\n")
        list1.append(guess)

    print(stages[lives])

    if lives == 0:
        print("********************You Loose!**********************")
        game_over = True

    if "_" not in display:
        print("******************You win!*********************")
        game_over = True
print(f"The Word was {chosen_word}")