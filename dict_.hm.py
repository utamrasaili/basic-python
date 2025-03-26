student = {}


roll= input("Enter the roll number: ")


name = input("Enter name: ")
age = int(input("Enter age: "))


math_grade = int(input("Enter Math grade: "))
history_grade = int(input("Enter History grade: "))
science_grade = int(input("Enter Science grade: "))


email = input("Enter email: ")
phone1 = int(input("Enter phone number 1: "))
phone2 = int(input("Enter phone number 2: "))


student[roll] = {
 'name': name,
 'age': age,
 'grades': {
 'math': math_grade,
 'history': history_grade,
 'science': science_grade
 },
 'contact': {
 'email': email,
 'phone': [phone1, phone2]
 }
}


# print(student)
grades = student['grades']
sum_of_grades = sum(grades.values())

print("Sum of grades:", sum_of_grades)
