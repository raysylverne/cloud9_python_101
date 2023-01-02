name = ""
while name != "exit":
    name = input( "What is your name: ")
    if len(name) >= 8:
        print("Your name is to loog")
    elif len(name) == 7:
        print(f"Your name is {name}")
    else:
        print("Your name is too short!")