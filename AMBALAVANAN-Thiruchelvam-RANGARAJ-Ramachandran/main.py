import csv
import random

def read_questions(file_path, num_questions=20):
    """
    Read a CSV file containing questions and answers, randomly select a specified number of questions,
    and return a list of dictionaries with question details.

    Parameters:
    - file_path (str): The path to the CSV file.
    - num_questions (int): The number of questions to randomly select (default is 20).

    Returns:
    - list: A list of dictionaries containing question details.
    """
    questions = []

    # Read CSV file and store questions in a list
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # Skip header row
        questions = [row for row in reader]

    # Randomly select 20 unique questions
    selected_questions = random.sample(questions, min(num_questions, len(questions)))

    # Create a dictionary with questions, answers, and the correct answer
    question_dict_list = []
    for row in selected_questions:
        question_dict = {
            'question': row[2],
            'answers': [row[3], row[4], row[5]],
            'correct_answer': int(row[1])
        }
        question_dict_list.append(question_dict)

    return question_dict_list

def print_questions_table(question_list):
    """
    Print a table with the selected questions, answers, and correct answer.

    Parameters:
    - question_list (list): A list of dictionaries containing question details.
    """
    # Print a table with the selected questions, answers, and correct answer
    print("{:<5} {:<70} {:<25} {:<25} {:<25}".format("No.", "Question", "Choice 1", "Choice 2", "Choice 3"))
    print("="*150)
    for i, question_dict in enumerate(question_list, 1):
        print("{:<5} {:<70} {:<25} {:<25} {:<25}".format(
            i,
            question_dict['question'],
            question_dict['answers'][0],
            question_dict['answers'][1],
            question_dict['answers'][2]
        ))

def get_candidate_name():
    """
    Prompt the user to enter the name of the candidate.

    Returns:
    - str: The name of the candidate.
    """
    candidate_name = input("Enter the name of the candidate: ")
    return candidate_name

def ask_for_footballer(candidate_name):
    """
    Ask the user to input the name of a footballer and print a personalized message.

    Parameters:
    - candidate_name (str): The name of the candidate.
    """
    footballer_name = input(f"Hello, {candidate_name}! Enter the name of your favorite footballer: ")
    print(f"{footballer_name} is a fantastic choice! Enjoy the football quiz.")

def take_quiz(questions):
    """
    Ask the user quiz questions, test the answers, and give a score.

    Parameters:
    - questions (list): A list of dictionaries containing question details.

    Returns:
    - tuple: A tuple containing user's answers and the final score.
    """
    score = 0
    user_answers = []

    for i, question_dict in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question_dict['question']}")
        for j, answer in enumerate(question_dict['answers'], 1):
            print(f"{j}. {answer}")

        user_answer = int(input("Your answer (enter the number): "))
        user_answers.append((i, user_answer))

        if user_answer == question_dict['correct_answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question_dict['correct_answer']}.")

    print(f"\nYour final score is: {score}/{len(questions)}")
    return user_answers, score

def identify_mistakes(questions, user_answers):
    """
    Identify and display the questions where the user's answers were incorrect, along with the correct answers.

    Parameters:
    - questions (list): A list of dictionaries containing question details.
    - user_answers (list): A list of tuples containing user's question number and answer.
    """
    mistakes = [(q_number, user_answer, questions[q_number - 1]['correct_answer']) for q_number, user_answer in user_answers if user_answer != questions[q_number - 1]['correct_answer']]

    if mistakes:
        print("\nMistakes:")
        print("{:<5} {:<70} {:<25} {:<25} {:<25} {:<25}".format("No.", "Question", "Your Answer", "Correct Answer", "Choice 1", "Choice 2", "Choice 3"))
        print("="*200)
        for q_number, user_answer, correct_answer in mistakes:
            question_dict = questions[q_number - 1]
            print("{:<5} {:<70} {:<25} {:<25} {:<25} {:<25}".format(
                q_number,
                question_dict['question'],
                user_answer,
                correct_answer,
                question_dict['answers'][0],
                question_dict['answers'][1],
                question_dict['answers'][2]
            ))
    else:
        print("\nNo mistakes! Great job!")

def save_result(candidate_name, questions, user_answers, final_score):
    """
    Save the results of the quiz to a text file named after the candidate.

    Parameters:
    - candidate_name (str): The name of the candidate.
    - questions (list): A list of dictionaries containing question details.
    - user_answers (list): A list of tuples containing user's question number and answer.
    - final_score (int): The final score of the candidate.
    """
    file_name = f"{candidate_name}_quiz_results.txt"
    with open(file_name, 'w') as file:
        file.write(f"Quiz Results for {candidate_name}\n")
        file.write("="*50 + "\n\n")
        file.write(f"Final Score: {final_score}/{len(questions)}\n\n")

        file.write("Question-wise Results:\n")
        for q_number, user_answer in user_answers:
            question_dict = questions[q_number - 1]
            file.write(f"\nQuestion {q_number}: {question_dict['question']}\n")
            file.write(f"Your Answer: {user_answer}\n")
            file.write(f"Correct Answer: {question_dict['correct_answer']}\n")
            file.write(f"Choices: {', '.join(question_dict['answers'])}\n")
            file.write("="*50 + "\n")

    print(f"Quiz results have been saved to {file_name}")

# Example usage
file_path = 'questions_and_answers.txt'
selected_questions = read_questions(file_path)
print_questions_table(selected_questions)

# Get the name of the candidate
candidate_name = get_candidate_name()

# Ask for the name of a footballer
ask_for_footballer(candidate_name)

# Take the quiz interactively
user_answers, final_score = take_quiz(selected_questions)

# Save the results
save_result(candidate_name, selected_questions, user_answers, final_score)