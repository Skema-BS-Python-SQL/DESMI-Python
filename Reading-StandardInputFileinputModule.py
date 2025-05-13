# need to be called python3 script.py filetoload.txt
# or on replit Shell not Console => 
# python main.py filetoload.txt
import fileinput

for fileinput_line in fileinput.input('filetoload.txt'):
    if 'Exit' == fileinput_line.rstrip():
        break
    print(f'Processing Message from fileinput.input() \n ***** {fileinput_line} *****')

print("Done")
