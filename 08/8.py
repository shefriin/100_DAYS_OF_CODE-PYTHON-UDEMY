def caesar(direction,text,shift):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    ceaser_text = ""
    for i in text:
        if i.isalpha() == False:
            ceaser_text += i
            continue
        pos = 0 # or just give shift *= -1 if decode , then no need of pos = 0 and all these if statements... AND NOTEE THAT THIS IF STMT IS OUT OF THIS FOR LOOP TO WORK PROPERLY
        if direction == "encode":
            pos = alphabet.index(i) + shift
        elif direction == "decode":
            pos = alphabet.index(i) - shift        
        pos %= 26
        ceaser_text += alphabet[pos]
    print(f"Here is the {direction}d result:{ceaser_text}")

print("""                                         
  /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$ 
 /$$_____/ |____  $$ /$$__  $$ /$$_____/ |____  $$ /$$__  $$
| $$        /$$$$$$$| $$$$$$$$|  $$$$$$   /$$$$$$$| $$  \__/
| $$       /$$__  $$| $$_____/ \____  $$ /$$__  $$| $$      
|  $$$$$$$|  $$$$$$$|  $$$$$$$ /$$$$$$$/|  $$$$$$$| $$      
 \_______/ \_______/ \_______/|_______/  \_______/|__/      

           /$$           /$$                                
          |__/          | $$                                
  /$$$$$$$ /$$  /$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$       
 /$$_____/| $$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$      
| $$      | $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/      
| $$      | $$| $$  | $$| $$  | $$| $$_____/| $$            
|  $$$$$$$| $$| $$$$$$$/| $$  | $$|  $$$$$$$| $$            
 \_______/|__/| $$____/ |__/  |__/ \_______/|__/            
              | $$                                          
              | $$                                          
              |__/
        """)
while 1:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your mesage:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    continue_game = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if continue_game != "yes":
        print("Goodbye!")
        break