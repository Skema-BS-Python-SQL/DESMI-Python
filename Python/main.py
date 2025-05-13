import csv
# Specify the path to your CSV file
result_file_path = 'results.csv'
file_path = 'questions_and_answers.txt'

# Initialize lists to store each component
question_numbers = []
right_answer_numbers = []
questions = []
answers_1 = []
answers_2 = []
answers_3 = []

# Open the file in read mode ('r' stands for read)
with open(file_path, 'r') as file:
    # Read and process each line in the file
    for line_number, line in enumerate(file, start=1):
        # Split the line into components using semicolons
        components = line.strip().split(';')

        # Check if the line has the expected number of components
        if len(components) == 6:
            # Extract individual components and store them in lists
            question_numbers.append(int(components[0]))
            right_answer_numbers.append(int(components[1]))
            questions.append(components[2])
            answers_1.append(components[3])
            answers_2.append(components[4])
            answers_3.append(components[5])
        else:
            print(f"Warning: Line {line_number} does not have the expected number of components.")

# Ask for the user's name
player_name = input("Enter your name: ")

# Ask the user each question
results = []  # List to store results
total_questions = len(question_numbers)
correct_answers = 0

for i in range(total_questions):
    print(f"Question {question_numbers[i]}: {questions[i]}")
    print(f"  1. {answers_1[i]}")
    print(f"  2. {answers_2[i]}")
    print(f"  3. {answers_3[i]}")

    valid_answer = False
    while not valid_answer:
        # Prompt user for input
        user_input = input("Your answer (enter 1, 2, or 3): ")

        # Check if the user's input is valid
        if user_input in ['1', '2', '3']:
            valid_answer = True
        else:
            print("Enter a valid answer (1, 2, or 3)")

    # Check if the user's input is correct
    result = {
        'PlayerName': player_name,
        'CorrectAnswer': right_answer_numbers[i],
        'Correct': int(user_input) == right_answer_numbers[i]
    }

    results.append(result)

    if result['Correct']:
        correct_answers += 1
        print("Correct!\n")
    else:
        print(f"Wrong! The correct answer is {right_answer_numbers[i]}\n")

# Calculate the final score
final_score = (correct_answers / total_questions) * 100
print(f"Your final score is: {final_score:.2f}%")

# Add final score to the results
result = {
    'PlayerName': player_name,
    'FinalScore': final_score
}
results.append(result)

# Write results to CSV file
with open(result_file_path, 'a', newline='') as csv_file:
    fieldnames = ['PlayerName', 'CorrectAnswer', 'Correct', 'FinalScore']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Check if the file is empty and write header if necessary
    if csv_file.tell() == 0:
        writer.writeheader()

    writer.writerows(results)