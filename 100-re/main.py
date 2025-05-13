import csv
import re

def validate_name(name):
    return re.match(r'^[A-Za-z\s]+$', name)

def validate_date(date):
    return re.match(r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(19|20)\d{2}$', date)

def validate_student_number(student_number):
    return re.match(r'^[A-Za-z0-9]+$', student_number)

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