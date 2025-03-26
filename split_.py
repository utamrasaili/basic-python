# num1=int(input("enter first number something"))
# num2=int(input("enter second number something"))


# result=num1+num2

# print(f"result {num1}+{num2} =",result)

#list denote by sign [ ]


# number=[1,2,3,4,5]
# fruits=['apple','banana','cherry']
# mixed_list=[10,'hello',True,3.14]
# print(number[0:1])
# print(fruits[2:])
# print(mixed_list[3:])


list
x="hello#world#python"
y=x.split("#")
print(y)

# input=["hello","world","python"]
# output="helloworldpython"
# output1="hello,world,python"
# output2="hello#world#python"
# output3="hello world python"

#output="".join(input)
#output1=",".join(input)
#output2="#".join(input)
#output3=" ".join(input)

# print(output)
# print(output1)
# print(output2)
# print(output3)

#string methods
#isdigit()

# s="12345"
# print(s.isdigit())
# #isupper()
# s="HELLO"
# print(s.isupper())

# #islower
# s="hello"
# print(s.islower())

#modifying list

#homework
# numbers=[1,2,3,4,5,6,7,8,9,10]
# print(numbers)

# x=input("enter the number to be replace")
# y=input("enter the new number")
# numbers[]=y




#question(2)
# #define the list of numbers
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# while True:
#     print(numbers)

#     choice= input ("enter y for replace,  press another for exits:")
#     if choice.lower()=="y":

#         old_value = int(input("enter the numbers to replace"))
#         new_value=int(input("enter the new number"))
#         for x in range (len(numbers)):
#             if numbers[x]==old_value:
#                 numbers[x]=new_value
#     else:
#         break
#     print(numbers)     



# # Print the original list
# print("Original List:", numbers)

# # Get user input for the number to replace and the new number
# x = int(input("Enter the number to replace: "))
# y = int(input("Enter the new number: "))

# # Check if the number to replace exists in the list
# if x in numbers:
#     # Replace the number
#     numbers[numbers.index(x)] = y
#     print("Updated List:", numbers)
# else:
#     print("The number you want to replace is not in the list.")



#questiuon(1)
# fruits=[]

# while True:
#     x=input("enter fruits name or press 0 to exit:")
#     if x!="0":
#         fruits.append(x)
#     else:
#         print(fruits) 
#         break  
