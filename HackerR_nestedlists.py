'''
https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
Given the names and grades for each student in a Physics class.
Store them in a nested list and R
Print the name(s) of any student(s) that the second lowest grade.

Output Format:
Print the name(s) of any student(s) having the second lowest grade in Physics; 
if there are multiple students, order their names alphabetically and print each 
one on a new line.
'''
students_grades=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_grades.append([name, score])


students_grades.append([name,score]) # populate the users input into nested list
# EXAMPLE OUTPUT: [["char", 55.5], ["beta", 75.0], ["alpha", 55.5], ["delta", 92.7]]
grades_list = sorted(list(set([student[1] for student in students_grades]))) # ⬇refer to Cliff notes for breakdown ⬇ 
# EXAMPLE OUTPUT: [55.5, 55.5, 75, 92.7]  
second_lowest_grade = grades_list[1]  # the second lowest grade will be at the [1] index in our grades_list
# EXAMPLE OUTPUT: #55.5
all_students_w_second_lowest = [ 
    student 
    for student in students_grades 
    if student[1] == second_lowest_grade
    ]
# EXAMPLE OUTPUT: [["alpha", 55.5], ["char", 55.5]]

all_students_w_second_lowest.sort()
for student in all_students_w_second_lowest:
    print(student)

# Given the names and grades for each student in a class N of  students, 
# store them in a nested list and print the name(s) of any student(s) having the 
# second lowest grade.
# create the nested list
# find the second lowest
# create a new list where the student grade matches with the second lowest grade
# sort them in alphabetiacl order and print

# EXAMPLE OUTPUT: student_grades=[["alpha", 55.5], ["beta", 75.0], ["char", 55.5], ["delta", 90.1]]

'''
 ⬇grades_list Cliff Notes ⬇
student_grades.append([name, score]) # will populate the users input in the form of a nested list 
list() function will creates a new list
sorted() function will sort all items in ascending order
set() Sets are used to store multiple items in a single variable. 
set() Since there can be duplicate grades we are passing the set function
# grades_list variable will iterate through the nested list "student_grades" and extract just the student grade "student[1]" 
⬇all_students_w_second_lowest liff Notes⬇
This variable will iterate through student_grades list and if the item at index[1] matches a second_lowest_grade then
it will populate into this list ll_students_w_second_lowest_grade list
'''