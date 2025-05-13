# need to be called python3 script.py cars.csv
# or python main.py cars.csv
#
import fileinput
for fileinput_line in fileinput.input("cars.csv"):
    if 'Exit' == fileinput_line.rstrip():
      break
    print(f'Processing Message from fileinput.input() *****\n{fileinput_line}*****')

print("Done")
