#7: Conditional Statements
#
# Can you write a Python program that collects student data, validates the input based on specific criteria, and appends the data to a CSV file without overwriting previous entries?  First and last names contain only text characters and spaces.  The date of birth follows the format (DD/MM/YYYY).  The student number contains only alphanumeric characters. Not use re (regular expression) for testing . Please use basic syntax suitable for beginners, and explain each part of the code.
#
import csv

def validate_name(name):
    return all(c.isalpha() or c.isspace() for c in name)

def validate_date(date):
    try:
        day, month, year = map(int, date.split('/'))
        if 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2099:
            return True
    except ValueError:
        pass
    return False

def validate_student_number(student_number):
    return student_number.isalnum()

def collect_student_data():
    first_name = input("Enter first name: ")
    while not validate_name(first_name):
        print("Invalid input. Name can only contain letters and spaces.")
        first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    while not validate_name(last_name):
        print("Invalid input. Name can only contain letters and spaces.")
        last_name = input("Enter last name: ")

    dob = input("Enter date of birth (DD/MM/YYYY): ")
    while not validate_date(dob):
        print("Invalid input. Date format should be DD/MM/YYYY.")
        dob = input("Enter date of birth (DD/MM/YYYY): ")

    student_number = input("Enter student number: ")
    while not validate_student_number(student_number):
        print("Invalid input. Student number can only contain alphanumeric characters.")
        student_number = input("Enter student number: ")

    return [first_name, last_name, dob, student_number]

def save_student_data_to_csv(data):
    with open('student_data.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(data)
    print("Data saved to student_data.csv")

def main():
    student_data = collect_student_data()
    save_student_data_to_csv(student_data)

if __name__ == "__main__":
    main()