# https://docs.python.org/3/library/csv.html
from csv import reader
# read csv file as a list of lists
with open('cars.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    # we use delimiter=';' for CSV use ;
    csv_reader = reader(read_obj, delimiter=';')
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)

#print(list_of_rows[2][0], list_of_rows[2][4])

#print(list_of_rows[2][0]) # Car
#print(list_of_rows[2][0]) # Buick Skylark 
#print(list_of_rows[1][0]) # STRING
#print(list_of_rows[0][2]) # Cylinders
#print(list_of_rows[2][2]) # Cylinders
#header = list_of_rows[0]
#print("Full list =>\n" + str(header))
#print("\n")
#header.remove('Car')
#print(header)
#print("\n")
#header.pop(0)
#print(header)
#print("\n")

for element in list_of_rows:
#  print(element[0],element[4])
#  
  if element[4] == '99999':
    print(element[0],element[4])

  

