# Using a for loop to print the message
for i in range(1, 6):
  print(f"Iteration {i}: Hello, World!")
  # you need to use str() to convert number to string
  # not possible to concatenate different formt
  print("Iteration " + str(i) + ": Hello, World!")