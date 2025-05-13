


file_obj = open("questions_and_answers.txt", "r")

def calculate_score(quiz, user_responses):
    score = 0
    for i, question in enumerate(quiz):
        user_answer = user_responses[i]
        correct_answer = question['CorrectAnswer']
        if user_answer.lower() == correct_answer.lower():
            score += 1
    return score

def retry_quiz():
    retry = input("\nYour score is less than 10. Do you want to retry the quiz? (yes/no): ")
    return retry.lower() == 'yes'

# Get player information
player_name = input("Enter your name: ")
player_age = int(input("Enter your age: "))

while True:
    # Load the CSV file into a list of dictionaries
    csv_file_path = 'questions_and_answers.txt'
    questions = []

    with open(csv_file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')  # Specify the delimiter
        for row in csv_reader:
            questions.append(row)

    # Check if the CSV file has at least 20 questions
    if len(questions) < 20:
        print("Error: The CSV file should contain at least 20 questions.")
        exit()

    # Initialize variables
    selected_indices = set()
    user_responses = []

    # Randomly select 20 unique questions
    while len(selected_indices) < 20:
        index = random.randint(0, len(questions) - 1)
        selected_indices.add(index)

    selected_questions = [questions[i] for i in selected_indices]

    # Format the selected questions into a quiz
    quiz = []
    for question in selected_questions:
        quiz.append({
            'Question': question[2],  # Change index to 2 for the question
            'Options': [question[3], question[4], question[5]],  # Change indices accordingly
            'CorrectAnswer': question[1]  # Change index to 1 for the correct answer
        })

    # Display welcome message
    print("\nWelcome to skema quiz!")
    print(f"\nPlayer Information:")
    print(f"Name: {player_name}")
    print(f"Age: {player_age}")

    # Display the quiz and get user responses
    for i, question in enumerate(quiz, start=1):
        print(f"\nQuestion {i}: {question['Question']}")
        for j, option in enumerate(question['Options'], start=1):
            print(f"   {j}. {option}")
        user_answer = input("Your answer: ")
        user_responses.append(user_answer)

    # Calculate the score
    score = calculate_score(quiz, user_responses)
    print(f"\nYour Score: {score}/{len(quiz)}")

    # Save user responses and correct answers to a new CSV file
    output_file_path = 'score file.csv'
    with open(output_file_path, 'w', newline='') as csvfile:
        fieldnames = ['PlayerName', 'PlayerAge', 'Question', 'Options', 'CorrectAnswer', 'UserResponse']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()
        for i, question in enumerate(quiz):
            csv_writer.writerow({
                'PlayerName': player_name,
                'PlayerAge': player_age,
                'Question': question['Question'],
                'Options': question['Options'],
                'CorrectAnswer': question['CorrectAnswer'],
                'UserResponse': user_responses[i]
            })

    # Display a message based on the user's score
    if score >= 16:
        print("Good Job !")
    elif 10 <= score < 16:
        print("Retry, you can do better.")
    else:
        print("Google it ")

    # Display correct and incorrect answers
    print("\nAnswers:")
    for i, (question, user_answer) in enumerate(zip(quiz, user_responses), start=1):
        correct_answer = question['CorrectAnswer']
        if user_answer.lower() != correct_answer.lower():
            print(f"Question {i}: Incorrect. Your answer: {user_answer}. Correct answer: {correct_answer}")
        else:
            print(f"Question {i}: Correct.")

    # Ask the user if they want to retry the quiz
    if score < 10 and not retry_quiz():
        break  # Exit the loop if the user does not want to retry