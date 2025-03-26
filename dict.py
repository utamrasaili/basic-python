# my_dict={"name":"alice",
#         "age":"30",
#         "city":"new york"
# }
# print(my_dict["name"])


# mixed_dict={
#     1:"one",
#     "2":"two",
#     (1,2):"tuple"
# }

# print(mixed_dict[1])
# print(mixed_dict.get("name","123"))



# name
# rollno
# address
# if press 1 add
# ask user what should be key
# ask user what should be value
 

# if press 2 update
# ask user which key value to updated
# what is the Value

# if press 3 to delete
# ask user which key should delete


# key = input("Enter the key (e.g., name, rollno, address): ")
# value = input(f"Enter the value for {key}: ")
# student[key] = value
# print(f"Student data added: {key} - {value}")


 
# student = {}
 
 
 
# while True:
#     print("""
# press 0 for view students
# press 1 for add
# press 2 for update
# press 3 for remove
# press 4 for exit
# """)
#     choice = int(input("enter the choice"))
 
#     if choice == 1:
#         print("We are adding new key value pair ")
#         k = input("enter the new key")
#         v = input("enter the new value")
#         student[k] = v
 
#     elif choice == 2:
#         print("We are updating existing value ")
#         print("student",student)
#         k = input("enter the key for which value should be updated")
#         v = input("enter the new value")
#         student[k] = v
 
 
#     elif choice == 3:
#         print("We are deleting existing key value ")
#         print("student",student)
#         k = input("enter the key for deleting")
#         student.pop(k)
 
#     elif choice == 0:
#         print("student",student)
   
#     elif choice == 4:
#         break
 
#     else:
#         print("invalid choice enter")
 
# student{}
# how can i solve this to make output as following

# output{"name":"abc",
#        "age":"12",
#        "address":"ktm",
#        "class":"4",
#        "phonenumber":[12345678,9854362711],
#        "marks":[12,23,55,55],
#        "totalmarks":145
# }
        
student = {}
 
 
 
while True:
    print("""
press 0 for view students
press 1 for add
press 2 for update
press 3 for remove
press 4 for exit
press 5 for sum
""")
    choice = int(input("enter the choice"))
 
    if choice == 1:
        print("We are adding new key value pair ")
        k = input("enter the new key")
        v = input("enter the new value")
        student[k] = v
 
    if choice ==5:
        print("we are adding value of marks")
        k=input()
 

# nested dictionary
 
grades = student['grades']

sum_of_grades = sum(grades.values())

print("Sum of grades:", sum_of_grades)


# homework


student={
    'roll1':{
     'name':'alice',
     'age':20,
    'grades':{
        'math':90,
        'history':85,
        'sciene':95
    },'contact':{
        'email':'alice@example.com',
        'phone':'123-345-678'}

      }
 }


# Access the grades dictionary
grades = student['roll1']['grades']

# Calculate the sum of the grades
sum_of_grades = sum(grades.values())

# Print the sum of the grades
# print(sum_of_grades =student['roll1']['grades']
phone=student['roll1']['contact']['phone']
print(phone)


sum=0
for x in phone:
    sum=sum+x
    print(sum)




student = {
    'roll1':{
    'name':"Alice",
    'age':20,
    'grades':{
        'math': 90,
        'history':85,
        'science':80
    },
    'contact':{
        'email':'alice@example.com',
        'phone':[123456789,987654321]
    }
    }
}

new_phone_number = 97234573838
student['roll1']['contact']['phone'].append(new_phone_number)

print(student)



 
 
roll1 = {
}
 
name = input("enter name")
 
age = int(input("enter age"))

 
roll1["name"] = name
roll1["age"] = age
print(roll1)
 
student = {"roll1":{'name': 'rohan', 'age': 123}}
roll = input("enter the roll number")
student[roll]= roll1
 
print(student)