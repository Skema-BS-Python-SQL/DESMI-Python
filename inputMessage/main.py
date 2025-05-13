# Loop get input and use 'Exit' keyword
# to quit the loop
# ''""(){}[]\`|
while True:
  data = input("Please enter the message:\n")
  if 'Exit' == data:
    break
  print(f'Processing Message from input() \n***** {data} *****')

print("Done")
