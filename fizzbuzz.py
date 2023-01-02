# print a pre-determine output based on user input 
user_value = ""
while user_value != "exit":
    user_value = int(input("Enter an number: "))
    # If the user provided you with a number that is a multiple of 3 and 5  print fizz buzz
    if user_value % 5 == 0 and user_value % 3 == 0:
        print("fizzbuzz")
    # If the user provided you with a number that is a multiple of 3 print fizz
    elif user_value % 3 == 0:
        print("Fizz")
    # If the user provided you with a number that is a multiple of 5 print buzz   
    elif user_value % 5 == 0:
        print("buzz")
    else:
        print(f"{user_value} is not a multiple of 3 or 5")
