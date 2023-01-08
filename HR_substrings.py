# I need to go back and type in notes  on this. 

def count_substring(string, sub_string):
    full_s_length = len(string)
    sub_s_length = len(sub_string)
    count=0
    
    for i in range(full_s_length-sub_s_length+1):
       if(string[i:(i + sub_s_length)] == sub_string):
           count+= 1
           
    return count
   
   
string = input("Enter Long String: ").strip()
sub_string = input("Enter Sub String: ").strip()
    
count = count_substring(string, sub_string)
print(count)



# https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
