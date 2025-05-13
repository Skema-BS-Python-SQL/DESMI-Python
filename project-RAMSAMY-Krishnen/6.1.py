def is_text_and_spaces(input_str):
  return all(c.isalpha() or c.isspace() for c in input_str)

def is_valid_date_format(date_str):
  parts = date_str.split("/")
  if len(parts) != 3:
      return False
  day, month, year = parts
  if not (day.isdigit() and month.isdigit() and year.isdigit()):
      return False
  day, month, year = int(day), int(month), int(year)
  if not (1 <= day <= 31 and 1 <= month <= 12):
      return False
  return True

def is_alphanumeric(input_str):
  return input_str.isalnum()

print("Please fill in the following details:")
first_name = input("First Name: ")
last_name = input("Last Name: ")
birth = input("Date of Birth (DD/MM/YYYY): ")
student_number = input("Student Number: ")

if (is_text_and_spaces(first_name) and
      is_text_and_spaces(last_name) and
      is_valid_date_format(birth) and
      is_alphanumeric(student_number)):
  with open("student_data.csv", "a") as file:
      file.write(f"{first_name},{last_name},{birth},{student_number}\n")
  print("Data saved successfully!")
else:
  print("Invalid input. Please check your input formats.")
