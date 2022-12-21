# Test Message
message = input("Enter a message: ")

print("First character:", message[0])
print("Last character:", message[-1])
# If the total characters are even then the character after dividing 
# by 2 will be identified as the middle exp: middle = (12/2) + 1
print("Middle character:", message[int(len(message) /2)])
print("Even index characters:", message[0::2])
print("Odd index characters:", message[1::2])
print("Reversed message:", message[::-1])
