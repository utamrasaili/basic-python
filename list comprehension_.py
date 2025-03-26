#question1
num=[1,1,1,2,2,2,2,3,4,5,6]
while 1 in num :
    num .remove (1)
print(num)
#when i remove 1 from num list # solve using remove ,pop clear 



#question2
num=[1,2,3,4,5,6]
newlist=num[::2]
print(newlist)
newlist=[]#result[1,3,5]

#question3
input=[1,2,3,4,5,6] #creat output list with power of 2 for each element on input list

#output=[1,4,9,16,25,36]
output =[ x**2 for x in input ]
print(output)
 #claswork   
input = [1,2,3,4,5,6]
new_list = [x if x%2 != 0 else "even" for x in input]
print(new_list)



