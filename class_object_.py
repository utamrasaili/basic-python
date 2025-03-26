class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age

  def greet(self):
     return f"hello,my name is {self.name} and I am {self.age}years old."
    
person1=person("uttam",30)
person2=person("bob",25)

print(person1.name)
print(person2.age)

message=person1.greet()
print(message)

