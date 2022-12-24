message = (input("Enter a Message: "))
print("Lowercase:", message.lower())
print("Uppercase: ", message.upper())
print("Capitalized: ", message.capitalize())
print("Title: ", message.title())

seperate = message.split()
print("Individual Words:", seperate)