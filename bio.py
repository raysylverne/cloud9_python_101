# Use #input() to ask user for input

name = input("What is your name? ")
color = input("what is your favorite color? ")
age = int(input("What is your age? "))

# use end= to dictate what happens at the end of line that is printed 
# in the example below it will add a single space

# print(name, end=" ")
# print("is " + str(age) + " years old", end=" ")
# print("and loves the color " + color + ".", end=" ")

# use sep=" " to dictate what goes inbetwen each value

print(name, 'is', age, 'years old and loves the color', color + '.', sep=" ")