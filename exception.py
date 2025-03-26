def divide(x,y):
    result=x/y
    print(result)

num1=int(input("enter the first number"))
num2=int(input("enter the second number"))


divide(num1,num2)




def divide():
    try:
        x = int(input("enter the number for x"))
        y = int(input("enter the number for y"))
        result = x / y
        print("result",result)
 
 
    # except Exception as e:
    #     print(f"error:{e}")
    #     x = int(input("enter the number for x"))
    #     y = int(input("enter the number for y"))
    #     result = x / y
    #     print("result",result)
 
 
    except ZeroDivisionError as e:
        print("you have enter the zero number for y")
        x = int(input("enter the number for x"))
        y = int(input("enter the number for y"))
        result = x / y
        print("result",result)
 
    except ValueError:
        print("you have enter the character ")
        x = int(input("enter the number for x"))
        y = int(input("enter the number for y"))
        result = x / y
        print("result",result)
 
divide()
 
def divide():
    try:
        x = int(input("enter the number for x"))
        y = int(input("enter the number for y"))
        result = x / y
        print("result",result)
 
 
    except Exception as e:
        print(f"error:{e}")
        x = int(input("enter the number for x"))
        y = int(input("enter the number for y"))
        result = x / y
        print("result",result)
 
 


x = int(input("enter the age"))
 
try:
    if x < 0:
        raise Exception("Sorry, no numbers below zero")
 
    elif x == 0:
        raise Exception("Sorry, age is zero")
 
except Exception as e:
    print(e)
    x = int(input("Re - Enter the age"))
 
# Created Custom Exception to handle different cases
 
class negative_error(Exception):
    def __init__(self,message):
        super().__init__(message)
class zero_error(Exception):
    def __init__(self,message):
        super().__init__(message)
 
x = int(input("enter the age"))
try:
    if x < 0:
        raise negative_error("Sorry, no numbers below zero")
 
    elif x == 0:
        raise zero_error("Sorry, age is zero")
except negative_error as e:
    print(e)
    print("you have enter the negative number")
    x = int(input("Re - Enter the age"))
except zero_error as e:
    print(e)
    print("Please enter the age based on month")
    x = int(input("etner the age based on month"))
    #age convert to year from month
 
 
 
# Raise Custom Exception to handle different cases with same Except block
 
 
x = int(input("enter the age"))
 
try:
    if x < 0:
        raise Exception("Sorry, no numbers below zero")
 
    elif x == 0:
        raise Exception("Sorry, age is zero")
 
except Exception as e:
    print(e)
    x = int(input("Re - Enter the age"))
 
 
 

 # Raise Custom Exception to handle different cases with same Except block
 
 
x = int(input("enter the age"))
 
try:
    if x < 0:
        raise Exception("Sorry, no numbers below zero")
 
    elif x == 0:
        raise Exception("Sorry, age is zero")
 
except Exception as e:
    print(e)
    x = int(input("Re - Enter the age"))
 
 
 
# Raise inbuilt Exception to handle different cases with same Except block
 
 
try:
    x = int(input("enter the number first"))
    y = int(input("enter the number second"))
    result = x / y
    print("result",result)
 
except Exception as e:
    print(e)
    x = int(input("enter the number first"))
    y = int(input("enter the number second"))
    result = x / y
    print("result")
 
# Raise inbuilt Exception to handle different cases with differebt Except block
 
try:
    x = int(input("enter the number first"))
    y = int(input("enter the number second"))
    result = x / y
    print("result",result)
 
except ZeroDivisionError as e:
    print(e)
    print("you have enter the zero value for number second")
    x = int(input("enter the number first"))
    y = int(input("enter the number second"))
    result = x / y
    print("result",result)
 
except TypeError as e:
    print(e)
    print("you have enter the character instead of number")
    x = int(input("enter the number first"))
    y = int(input("enter the number second"))
    result = x / y
    print("result",result)
 
 
 
 
 
 
 # Created Custom Exception to handle different cases
 
class negative_error(Exception):
    def __init__(self,message):
        super().__init__(message)
   
class zero_error(Exception):
    def __init__(self,message):
        super().__init__(message)
 
x = int(input("enter the age"))
try:
    if x < 0:
        raise negative_error("Sorry, no numbers below zero")
 
    elif x == 0:
        raise zero_error("Sorry, age is zero")
except negative_error as e:
    print(e)
    print("you have enter the negative number")
    x = int(input("Re - Enter the age"))
except zero_error as e:
    print(e)
    print("Please enter the age based on month")
    x = int(input("etner the age based on month"))
    #age convert to year from month
 
 
 
 
 
 
 
 
 
 
 