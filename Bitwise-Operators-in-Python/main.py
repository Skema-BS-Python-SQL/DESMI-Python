# Permissions
READ = 0b100  # 4 in decimal, can be obtain by bin(4)
WRITE = 0b010  # 2 in decimal, can be obtain by bin(2)
EXECUTE = 0b001  # 1 in decimal, can be obtain by bin(1)

# Sample file permissions (Read and Write permissions set)
file_permissions = 0b110  # 6 in decimal

# Check if the file has Write permission
has_write_permission = file_permissions & WRITE
if has_write_permission:
    print("File has write permission!")
else:
    print("File does not have write permission!")

# Explaination
# Binary (base 2): bin(4)
# Octal (base 8): oct(4)
# Hexadecimal (base 16): hex(4)
#
# For the decimal number 4, the outputs would be:
#
# Binary: '0b100'
# Octal: '0o4'
# Hexadecimal: '0x4'
# The prefixes 0b, 0o, and 0x indicate binary, octal, and hexadecimal representations,
# respectively. If you want just the number without the prefix, you can use string slicing:
#
# binary_representation = bin(4)[2:]
# octal_representation = oct(4)[2:]
# hexadecimal_representation = hex(4)[2:]
# This will give you:
# Binary: '100'
# Octal: '4'
# Hexadecimal: '4'
