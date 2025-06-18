def add(n1, n2):
    return n1+n2
def subtract(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    return n1/n2
calculator = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide
}
print("""
 _____________________
|  _________________  |
| | SHEENU       0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
""")
num1 = float(input("What's the first number?: "))
while 1:
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    result = calculator[operation](num1,num2)
    print(f"{num1} {operation} {num2} = {result}")
    continue_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
    if continue_calculation == "y":
        num1 = result
    else:
        print("\n"*100)
        num1 = float(input("What's the first number?: ")) 
        # NOW RATHER THAN THIS HERE WE ACTUALLY TERMINATE THE CONTINUE_CALCULATION AND TERMINATE THE WHILE LOOP , SO HOW THIS AGAIN WORKS IS IN THIS PLACE WE CALL A FUNCTION OF ITSELF AGAIN THAT IS A RECURSIVE FUNCTION, OKAY IMAGINE ALL ALL OF THESE ARE INSIDE A CALC() FUNCTIN WHICH IS FIRST CALLED OUTSIDE THEN AGAIN CALLED ONCE AGAIN HERE, THAT IS NOW ALL OTHER MEMORY IS ERASED AND NEW VALUES ARE SET ON. SO HERE WE USE RECURSIVELY CALLING THE FUNCTION USING ENCLOSING THE WHOLE THING IN A FUNCTION THEN CALLING IT HERE AND OUTSIDE FIRST : TO WORK FOR THE FIRST TIME
