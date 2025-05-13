# Use 'Exit' keyword to kill the loop
#
welcome = "Use 'Exit' keyword at the prompt to kill the loop\n\n"
print(welcome)
while True:
    data = input("Please enter your message:\n")
    if 'Exit' == data:
        break
    print(f'Processing Message from input() \n***** {data} *****\n')

print("Done")