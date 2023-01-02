def validate_and_execute():
    try: 
    
        if len(name) >= 8:
            print("Your name is to loog")
        elif len(name) == 7:
            print(f"Your name is {name}")
        else:
            print("Your name is too short!")
    except ValueError:
        print("Your input is not a number don't crash the program")

name = ""
while name != "exit":
    name = input( "What is your name: ")
    validate_and_execute()