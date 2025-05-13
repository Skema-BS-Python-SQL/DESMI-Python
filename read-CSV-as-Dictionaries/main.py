# https://docs.python.org/3/library/csv.html
from csv import DictReader
# open file in read mode
with open('cars.csv', 'r') as read_obj:
    # pass the file object to DictReader() to get the DictReader object
    dict_reader = DictReader(read_obj, delimiter=';')
    # get a list of dictionaries from dct_reader
    list_of_dict = list(dict_reader)
    # print list of dict i.e. rows

#print(list_of_dict)
    
#print(list_of_dict[1]['Car']) # Car
#print(list_of_rows[2][0]) # Buick Skylark 
#print(list_of_rows[1][0]) # STRING
#print(list_of_rows[0][2]) # Cylinders
#print(list_of_rows[2][2]) # Cylinders

  
# Loop for read col 1 and 2
for row in list_of_dict:
  print(row['Car'], row['Cylinders'])
  
  if row['Origin'] == 'US':
    print(row['Car'], row['Cylinders'], row['Origin'])

  

