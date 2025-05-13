import sys
# Use 'Exit' keyword to kill the loop
#
welcome = "Use 'Exit' keyword at the prompt to kill the loop\n\n"
action = "Please enter your message:\n"
print(welcome)
print(action)

for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    print(f'Processing Message from sys.stdin \n***** {line} *****\n')

print("Done")
