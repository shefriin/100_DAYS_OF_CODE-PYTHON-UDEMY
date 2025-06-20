'''
import random 
num = random.randint(1,2)
if num == 1:
    print("Heads")
else:
    print("Tails")
'''
'''
import random 
friends = ["Alice","Bob","Charlie","David","Emanuel"]
num = random.randint(0,len(friends)-1)
print(friends[num])
person = random.choice(friends)
print(person)
'''
import random
s = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
p = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
r = '''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
list1 = [r,p,s]
choice_of_game = int(input("What do you choose? 0:Rock, 1:Paper, 2:Scissors: "))
if choice_of_game == 0:
    print(r)
elif choice_of_game == 1:
    print(p)
elif choice_of_game == 2:
    print(s)
else:
    print("Wrong choice!")
print("Computer chose:\n")
random_comp = random.choice(list1)
print(random_comp)
if random_comp == r:
    if choice_of_game == 0:
        print("It's a Tie!")
    elif choice_of_game == 1:
        print("You Win!")
    elif choice_of_game == 2:
        print("You Lost!")
elif random_comp == p:
    if choice_of_game == 0:
        print("You Lost!")
    elif choice_of_game == 1:
        print("It's a Tie! ")
    elif choice_of_game == 2:
        print("You Win!")
elif random_comp == s:
    if choice_of_game == 0:
        print("You Win!")
    elif choice_of_game == 1:
        print("You Lost!")
    elif choice_of_game == 2:
        print("It's a Tie! ")

#okay gais i just want to tell that think small, like how can you make all of these optimised, you are repetitinga all of these a whole lot times than required and thats not really the best practice. idk how to get the best logic thinking, i just think that when you finished writing your version of code, just look at it. Really look at it and just think how you can make it smaller and more good and wonderful and thats it bye!