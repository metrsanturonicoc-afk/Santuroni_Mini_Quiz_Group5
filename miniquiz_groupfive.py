# User Login 
def user_login():
    # Existing valid username & password
    correct_username = "Alwin Uno"
    correct_password = "123456789"

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check username and password
    if username == correct_username and password == correct_password:
        print(f"Welcome, {username}!\n")
        return True
    else:
        print("Incorrect username or password. Please try again.\n")
        return False


# True/False Mini Quiz
def run_quiz():
    questions = {
        "Python is a programming language. (True/False)": "True",
        "A while loop in Python runs as long as the condition is True. (True/False)": "True",
        "The keyword 'def' is used to define a function in Python. (True/False)": "True",
        "A while loop in Python executes a block of code only once, regardless of the condition. (True/False)": "False",
        "A for loop in Python is used to iterate over a sequence such as a list, tuple, or string. (True/False)": "True"
    }

    correct_answers = 0

    for question, correct_answer in questions.items():
        user_answer = input(question + " ").capitalize()
        if user_answer == correct_answer:
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"Your answer is wrong. The correct answer is {correct_answer}.\n")

    print(f"Quiz finished! You got {correct_answers} out of {len(questions)} correct.")


# Main program
if __name__ == "__main__":
    logged_in = False
    while not logged_in:
        logged_in = user_login()

    run_quiz()