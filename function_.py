 
#type1 parameter less function and no return type
def addition():
    num3 = int(input("enter the num3"))
    num4 = int(input("enter the num4"))
    result1 = num3 + num4
    print(result1)
 
addition()
 
 
 
 
 
#type2 parameter less function and return type
def addition():
 
    num3 = int(input("enter the num3"))
    num4 = int(input("enter the num4"))
    result1 = num3 + num4
    return result1
   
 
finalresult = addition()
 
 
#type3 parameter function and no return type
def addition(x,y):
   
    result1 = x + y
    print(result1)
 
 
 
num1 = int(input("enter the num1"))
num2 = int(input("enter the num2"))
 
 
addition(num1,num2)
 
addition(10,20)
 
 
 
 
 
#type4 parameter  function and return type
def addition(x,y):
 
   
    result1 = x + y
    return result1
   
num3 = int(input("enter the num3"))
num4 = int(input("enter the num4"))
finalresult = addition(num3,num4)
print(finalresult)
 


#
def addition(x,y):
 
    result1 = x + y
    return result1
 
def sub(x,y):
 
    result1 = x - y
    return result1
 
def ui(n):
    print(n)
 
ui("addition")
final1 = addition(5,6)
print(final1)
 
ui("subtract")
final2 = sub(final1,6)
 
#####
def addition(x,y):
    result1 = x + y
    return result1
 
def sub(x,y):
    result1 = x - y
    return result1
 
def div(x,y):
    result1 = x / y
    return result1
 
 
def mul(x,y):
    result1 = x * y
    return result1
 
def ui():
    print("""
    Enter the choice number
    1. Addition
    2. Substraction
    3. Multiplication
    4. Division
    5. Exit
    """)
 
while True:
    ui()
    choice = int(input("enter the choice"))
    num1 = int(input("enter the num1"))
    num2 = int(input("enter the num2"))
    if choice == 1:
        result = addition(num1,num2)
        print("addition",result)
 
 
    elif choice == 2:
        result = sub(num1,num2)
        print("sub",result)
 
 
 
    elif choice == 3:
        result = mul(num1,num2)
        print("mul",result)
 
 
    elif choice == 4:
        result = div(num1,num2)
        print("div",result)
 
    elif choice == 5:
        print("exiting.....")
        break
 
    else:
        print("invalid")
 


#  
 
result123 = 200
def my_function():
    global result123
    result123 = 10
    print("calling x from inside the function",result123)
 
 
 
my_function()
print("calling x from outside the function",result123)

 
#args
def addition(*args):
    print(type(args))
    print(args)
 
addition(1,2,3,4,5,6,7,5,7,7,8,8,9,9,9,99999,9,9,9,9,9,9,9)
 
#kwargs
 
def addition(**kargs):
    print(type(kargs))
    print(kargs)
 
addition(name="abc",roll=23)
 