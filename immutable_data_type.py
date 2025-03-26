# input = "#######helloworld#######"
# output = input.strip('#').replace("helloworld", "hello world")

# print(output)
# input = "#######helloworld#######"

# # Count the number of '#' characters
# num_hashes = input.count('#')

# print(f"Number of '#' characters: {num_hashes}")













# # s="-------hello world"
# # s=s.replace("hello","uttam").strip("-")
# # print(s)

# # print(s.replace("world","world"))

# # homework
# input="(#############helloworld##############)"
# # output="hello world"
# input=input.replace("helloworld", "hello uttam").strip("#")
# print(input)


output="#####helloworld###"
input="Hello World"
output="####"+input[:5].lower()+input[5:].lower()+"###"

print(output)
