import csv

def load_quiz_data(file_path):
    quiz_data = []

    try:
        with open(file_path, 'r', newline='') as file:
            csv_reader = csv.reader(file, delimiter=';')

            for row in csv_reader:
                # Assuming the CSV format: id;answer;question;option1;option2;option3
                question = {
                    "id": int(row[0]),
                    "answer": int(row[1]),
                    "question": row[2],
                    "options": row[3:]
                }
                quiz_data.append(question)

        return quiz_data

    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print(f"Error loading quiz data: {e}")
        return None

def get_user_info():
    name = input("Enter your name: ")
    return name

def ask_questions(questions):
    score = 0
    for i, question in enumerate(questions, start=1):
        print(f"Question {i}: {question['question']}")
        print("Options:")
        for idx, option in enumerate(question['options'], start=1):
            print(f"{idx}. {option}")

        user_answer = input("Your answer (enter option number): ")

        try:
            user_answer = int(user_answer)
            if user_answer == question['answer']:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
        except ValueError:
            print("Invalid input! Moving to the next question.")

    return score

def save_score(name, score):
    try:
        with open('scores.txt', 'a') as file:
            file.write(f"{name}: {score}\n")
        print("Score saved successfully!")
    except Exception as e:
        print(f"Error saving score: {e}")

def main():
    file_path = 'questions..csv'
    quiz_data = load_quiz_data(file_path)

    if quiz_data:
        print("Quiz data loaded successfully!")
        name = get_user_info()
        print(f"Welcome, {name}! Let's start the quiz.")

        user_score = ask_questions(quiz_data)
        print(f"Quiz complete! {name}, your score is: {user_score}/{len(quiz_data)}")

        save_score(name, user_score)

if __name__ == "__main__":
    main()

def test_load_quiz_data():
  file_path = 'questions.csv'
  quiz_data = load_quiz_data(file_path)
  assert quiz_data is not None, "Quiz data should not be None"
  assert len(quiz_data) > 0, "There should be questions loaded"

  print("load_quiz_data function test passed.")


test_load_quiz_data()

