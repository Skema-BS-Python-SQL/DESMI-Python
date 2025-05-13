#Using input() function to read stdin data
while True:
    data = input("Please enter the message:\n")
    if 'Exit' == data:
        break
    print(f'Processing Message from input() \n***** {data} *****')

print("Done")