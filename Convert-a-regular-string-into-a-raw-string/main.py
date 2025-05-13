# To convert a regular string into a raw strings = '\n'
s = '\n'
raw_string = repr(s)
print(raw_string)
# To remove the quote at the beginning 
# and end of the string, you can use slices
raw_string = repr(s)[1:-1]
print(raw_string)