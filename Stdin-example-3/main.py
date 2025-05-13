import fileinput
# Use 'Exit' keyword to kill the loop
#
welcome = "Use 'Exit' keyword at the prompt to kill the loop\n\n"
print(welcome)

for fileinput_line in fileinput.input():
    if 'Exit' == fileinput_line.rstrip():
        break
    print(
        f'Processing Message from fileinput.input() \n***** {fileinput_line} *****'
    )

print("Done")
