import csv
import random

def select_random_questions(file_name, num_questions=20):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=';')
            all_questions = [row for row in csv_reader]

        if len(all_questions) < num_questions:
            raise ValueError("Not enough questions in the file.")

        selected_questions = random.sample(all_questions, num_questions)

        question_dict = {}
        for question in selected_questions:
            question_text = question[2]
            correct_answer_index = int(question[1]) - 1  # Adjusting index to Python's 0-based indexing
            answers = question[3:6]

            question_dict[question_text] = {
                'correct_answer': answers[correct_answer_index],
                'answers': answers
            }

        return question_dict

    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return {}
    except ValueError as ve:
        print(ve)
        return {}

# Usage example
questions = select_random_questions('questions_and_answers.txt')
for question, details in questions.items():
    print(f"Question: {question}")
    print(f"Correct Answer: {details['correct_answer']}")
    print(f"Answers: {', '.join(details['answers'])}")
    print("-" * 20)
