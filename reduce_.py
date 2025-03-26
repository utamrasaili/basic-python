from functools import reduce 

numbers=[1,2,3,4,5]
# examle1 :summing up a list of numbers
sum =reduce(lambda x,y: x+y, numbers)
print(sum)

# example2:finding a maximum numbers in a list
numbers=[3,8,1,6,2]
max_num= reduce(lambda x,y :x if x>y else y,numbers)
print(max_num)

# example3:concatenating strings in a list
words=["Hello"," ","world","!"]
sentence= reduce(lambda x,y:x+y,words)
print(sentence)

# example 4:using a initializer
numbers=[1,2,3,4,5]
product=reduce(lambda x,y:x*y,numbers,1)
print(product)


# To check director
import os 

current=os.getcwd()

print(("path",current))
files=os.listdir(current)
print("files",files)


# random number check [jastai otp haru garni bella garni ho]

import random
# generate a random integer bvetween 1 to 10 
random_number=random.randint(1,10)
print(random_number)

# shuffle a list 
my_list =[1,2,3,4,5]
random.shuffle(my_list)
print(my_list) 

import math

# calculate the square root
sqrt_value = math.sqrt(25)
print(sqrt_value)

