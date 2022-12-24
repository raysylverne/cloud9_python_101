message = (input("Enter a Message: "))
print("Lowercase:", message.lower())
print("Uppercase: ", message.upper())
print("Capitalized: ", message.capitalize())
print("Title: ", message.title())

seperate = message.split()
print("Individual Words:", seperate)

sorted_words = sorted(seperate)
print("Alphabetic First Word:", sorted_words[0])
print("Alphabetic Last Word:", sorted_words[-1])