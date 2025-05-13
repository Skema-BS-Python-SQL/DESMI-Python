import csv
import random

def import_questions(file_name, num_questions=20):
    questions = {}
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        all_questions = list(reader)

        # Randomly select unique questions
        selected_questions = random.sample(all_questions, num_questions)

        for row in selected_questions:
            question_num = row[0]
            question = row[2]
            correct_answer = row[int(row[1]) + 2]
            wrong_answers = [row[i] for i in range(3, 6) if i != int(row[1]) + 2]

            answers = [correct_answer] + wrong_answers
            random.shuffle(answers)

            questions[question] = {
                "correct_answer": correct_answer,
                "answers": answers
            }

    return questions

def print_question_table(questions):
    print("Question | Correct Answer | Other Options")
    print("----------------------------------------")
    for question, data in questions.items():
        correct_answer = data["correct_answer"]
        other_options = data["answers"]

        print(f"Question: {question}")
        for i, option in enumerate(other_options, 1):
            print(f"{i}. {option}")

        user_answer = int(input("Your answer (Enter the number): "))
        if user_answer == other_options.index(correct_answer) + 1:
            print("Correct!\n")
        else:
            print(f"Wrong! Correct answer is {correct_answer}\n")

# Usage example
questions_dict = import_questions("questions_and_answers.txt")
print_question_table(questions_dict)


