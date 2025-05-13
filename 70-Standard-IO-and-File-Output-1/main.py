print("Please fill in the following details:")
first_name = input("First Name: ")
last_name = input("Last Name: ")
birth = input("Date of Birth (DD/MM/YYYY): ")
student_number = input("Student Number: ")

with open("student_data.csv", "w") as file:
    file.write("First Name,Last Name,Date of Birth,Student Number\n")
    file.write(first_name + "," + last_name + "," + birth + "," + student_number + "\n")

print("Data saved successfully!")