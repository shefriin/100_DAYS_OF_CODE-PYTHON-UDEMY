#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt") as main_file:
    content = main_file.read()

with open("Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()


for i in names:
    content = content.replace("[name]",i.strip())
    with open(f"Output/ReadyToSend/{i.strip()}.txt","w") as output_file:
        output_file.write(content)
    content = content.replace(i.strip(),"[name]")
    