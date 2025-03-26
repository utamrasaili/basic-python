

sub = lambda a,b :a-b
print(sub(12,8))

#  map()
lst =[1,2,3,4,]
for x in lst :
    print(x)

result=list(map(lambda x :x**2,lst)) #[list koo order ma akhya aru dict set ma ni rakhna miltheo]

def power(n):
 return n-1
result=set(map(power,lst))
print(result)

numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=list(filter(lambda x:x%2==0,numbers))
print(even_numbers)

def even(x):
    return x % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = set(filter(even, numbers))
print (even_numbers)
