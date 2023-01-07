'''
The provided code stub reads and integer, n, from STDIN. 
All non-negative integers that are i < n should be squared to the power of 2
Example

n = 3
The list of non-negative integers that are less than n = 3 is [0,1,2]
Print the square of each number on a separate line.
0
1
4
'''


n = int(input("Provide a number: "))

num_list = []
for i in range(0, n): # (0, 1, 2, 3,4)     4 == n-1
        num_list.append(i ** 2) # Using ** to get the square of each number that is in the r
# The .append will populate (0,1,4,9,16) to the empty num_list []
for i in num_list:    
    print(i)

'''
Changing out n for s I've decided to use list comprehension to shortent the 
syntax needed to get the same output. Doing is this way removes the need to append
'''

s = int(input("Provide a number: "))
squared_nums = [i ** 2 for i in range(0, s)]

for i in squared_nums:    
    print(i)
# n is taken in as input 5 [0,1,2,3,4]
