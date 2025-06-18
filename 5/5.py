'''
list1 = [1,2,5,7,8,45,120,99,74,56,852,149,54,25,36,70,12,95,88]
print(max(list1))
maxx = float('-inf') # or just 0
for i in list1:
    if maxx < i:
        maxx = i
print(maxx)
list1.sort(reverse=True)
print(list1[0])
'''
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','%','&','(',')','*','+']

print("Welcome to PyPassword Generator!")
letters_in_password = int(input("How many letters would you like in your password?\n"))
symbols_in_password = int(input("How many symbols would you like in your password?\n"))
nos_in_password = int(input("How many numbers would you like in your password?\n"))
password_easy = []
for i in range(letters_in_password):
    password_easy.append(random.choice(letters))
for i in range(symbols_in_password):
    password_easy.append(random.choice(symbols))
for i in range(nos_in_password):
    password_easy.append(random.choice(numbers))

print(password_easy)

random.shuffle(password_easy)
print(password_easy)

password_hard = []
list1=[1,2,3]
count_l = letters_in_password
count_s = symbols_in_password
count_n = nos_in_password
total = count_l+count_s+count_n
for i in range(total):
    choose = random.choice(list1)
    if choose == 1:
        password_hard.append(random.choice(letters))
        count_l -= 1
        if count_l == 0:
            list1.remove(1)
    elif choose == 2:
        password_hard.append(random.choice(symbols))
        count_s -= 1
        if count_s == 0:
            list1.remove(2)
    elif choose == 3:
        password_hard.append(random.choice(numbers))
        count_n -= 1
        if count_n == 0:
            list1.remove(3)
print(password_hard)
password_hard_string = ''.join(password_hard)
print(f"Your pasword is:{password_hard_string}")    
