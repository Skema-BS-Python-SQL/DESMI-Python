# Using sys.stdin to read from standard input
import sys
print("What's your name :\n")
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    print(f'Processing Message from sys.stdin \n Hello {line} ')
print("Done")