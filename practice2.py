
# import csv
# # data=[['alice','30','london']
# #       ['bob''23','paris']
# #       ['charlie','25','berlin']]


# file_path='output.csv'


# with open("/Users/uttamtolange/Desktop/python/data.csv",mode='w',newline='')as file:

#     csv_writer=csv.writer(file)

#     for row in csv_writer:
#         print(row)
#     csv_writer.writerrow(row)
    


import csv

with open("/Users/uttamtolange/Desktop/python/myfile.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        

#  ['name', 'age', 'job', 'city']
#  ['Bob', '25', 'Manager', 'Seattle']
#  ['Sam', '30', 'Developer', 'New York']


row= ['Bob', '25', 'Manager', 'Seattle']
print(row[0])
print(row[1])
print(row[2])


 
 








      
    