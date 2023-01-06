








# Write a program that prints the numbers from 1 - 100. 


user_input = int(input("How many items should we process: "))

for number in range(1, user_input + 1):
    if number % 5 == 0 and number % 3 == 0:  # Print "FizzBuzz" if the number is divisible by 3 and 5.
        print("fizzbuzz")
    elif number % 5 == 0: # Print "Buzz" if the number is divisible by 5.
        print("Buzz")
    elif number % 3 == 0:  # Print "Fizz" if the number is divisible by 3.
        print("Fizz")
    else:
        print(number) # Otherwise print the number.