# Permissions
READ = 0b100  # 4 in decimal
WRITE = 0b010  # 2 in decimal
EXECUTE = 0b001  # 1 in decimal

# Sample file permissions (Read and Write permissions set)
file_permissions = 0b110  # 6 in decimal

# Check if the file has Write permission
has_write_permission = file_permissions & WRITE

if has_write_permission:
    print("File has write permission!")
else:
    print("File does not have write permission!")
