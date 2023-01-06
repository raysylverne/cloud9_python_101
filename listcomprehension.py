colors = [ 'blue',  'green', 'red', 'orange', 'yellow']
uppercase_colors = []
for color in colors:
    uppercase_colors.append(color.upper())
#print(uppercase_colors)

# Here's a different way to get the same outcome

uppercase_colors = [color.upper() for color in colors]
#print(uppercase_colors)

 
'''
Inside of a list comprehension the code to the left of the "for statement"
Represents the expected outcome. Essentially that same as above with have 
the lines of code. This is easier to read and great for filtering
'''
warm_colors = []
for color in colors:
    if color in ['red', 'orange', 'yellow']:
        warm_colors.append(color)
print(warm_colors)

# pass conditionals within a list 
warm_colors = [ color for color in colors if color in ['red', 'orange', 'yellow']]
print(warm_colors)


# Just messing around to see what else can be done
uppercase_colors = [color.replace('blue', 'pink') for color in colors]
print(uppercase_colors)


