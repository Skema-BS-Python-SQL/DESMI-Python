mydict = [{"color":"blue","doilike":"yes"},   {"color":"red","doilike":"no"}]

print(mydict[0]['color'])

list_of_rows = list(mydict)

for element in list_of_rows:
  print(element['color'])

