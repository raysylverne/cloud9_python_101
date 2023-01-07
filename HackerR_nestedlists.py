student_grades=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_grades.append([name, score]) # populate ther users input into 


grades_list = sorted(list(set([student[1] for student in student_grades]))) # refer to notes at⬇️
second_lowest_grade = grades_list[1] 



# Given the names and grades for each student in a class N of  students, 
# store them in a nested list and print the name(s) of any student(s) having the 
# second lowest grade.
# create the nested list
# find the second lowest
# create a new list where the student grade matches with the second lowest grade
# sort them in alphabetiacl order and print

# EXAMPLE: student_grades=[["alpha", 55.5], ["beta", 75.0], ["char", 55.5], ["delta", 90.1]]

'''
grades_list Cliff Notes
student_grades.append([name, score]) # will populate the users input in the form of a nested list 
list() function will creates a new list
sorted() function will sort all items in ascending order
set() Sets are used to store multiple items in a single variable. 
set() Since there can be duplicate grades we are passing the set function
# grades_list variable will iterate through the nested list "student_grades" and extract 
just the student grade "student[1]" 

'''