s = 'lang\tver\nPython\t3'
print(s)
# However, raw strings treat the backslash (\) as a literal character. For example:
s = r'lang\tver\nPython\t3'
print(s)
# A raw string is like its regular string with the backslash (\) represented as double backslashes (\\):
s1 = r'lang\tver\nPython\t3'
s2 = 'lang\\tver\\nPython\\t3'
print(s1 == s2) # True
#In a regular string, Python counts an escape sequence as a single character:
s = '\n'
print(len(s)) # 1
# However, in a raw string, Python counts the backslash (\) as one character:
s = r'\n'
print(len(s)) # 2