import time
from termcolor import colored

# Function to record participant's response
def record_response(question, options):
    print(question)
    for i, option in enumerate(options):
        print(f"{chr(65 + i)}) {option}")
    start_time = time.time()
    response = input("Your answer (A/B/C/D): ").upper()
    end_time = time.time()
    response_time = end_time - start_time
    return response, response_time




# Function to display results
def display_results(results):
    print("\n---- Results ----")
    for i, result in enumerate(results):
        question_num = i + 1
        question = result[0]
        response = result[1]
        response_time = result[2]
        correct = result[3]
        print(f"Question {question_num}:")
        print(f"Question: {question}")
        print(f"Response: {response}")
        print(f"Response Time: {response_time:.2f} seconds")
        print(f"Correct: {correct}")
        print("------------------")

# Stroop experiment questions and answers
questions = [
    (colored("Question 1: What color is the word written in? RED", "blue"),
     [colored("Red", "red"), colored("Blue", "blue"), colored("Green", "green"), colored("Yellow", "yellow")], "B"),
    (colored("Question 2: What color is the word written in? BLUE", "green"),
     [colored("Green", "green"), colored("Yellow", "yellow"), colored("Red", "red"), colored("Blue", "blue")], "A"),
    (colored("Question 3: What color is the word written in? GREEN", "yellow"),
     [colored("Yellow", "yellow"), colored("Green", "green"), colored("Red", "red"), colored("Blue", "blue")], "A"),
    (colored("Question 4: What color is the word written in? YELLOW", "blue"),
     [colored("Blue", "blue"), colored("Green", "green"), colored("Yellow", "yellow"), colored("Red", "red")], "A"),
    (colored("Question 5: What color is the word written in? RED", "yellow"),
     [colored("Red", "red"), colored("Blue", "blue"), colored("Green", "green"), colored("Yellow", "yellow")], "D"),
     (colored("Question 6: What color is the word written in? PURPLE", "magenta"),
     [colored("Yellow", "yellow"), colored("Grey", "grey"), colored("Black", "black"), colored("Magenta", "magenta")], "D"),
    (colored("Question 7: What color is the word written in? ORANGE", "cyan"),
     [colored("Grey", "grey"), colored("Red", "red"), colored("Cyan", "cyan"), colored("White", "white")], "C")
    # Add more questions here
]

# Participant details
participant_name = input("Enter your name: ")

# Perform the experiment
results = []
for question, options, correct_answer in questions:
    response, response_time = record_response(question, options)
    correct = response == correct_answer
    results.append((question, response, response_time, correct))
    print("\n")

# Display the results
display_results(results)
