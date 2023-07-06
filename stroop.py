import select
import sys
import time
import threading
from termcolor import colored
from song_timing import perform_song_timing
import random


# Variable to store participant's response
participant_response = None

# Function to read participant's response
def read_response():
    global participant_response
    rlist, _, _ = select.select([sys.stdin], [], [], 10)  # Wait for 3 seconds for input
    if rlist:
        participant_response = sys.stdin.readline().strip().upper()




# Function to record participant's response
def record_response(question, options):
    global participant_response
    participant_response = None  # Reset participant response
    print(question)
    for i, option in enumerate(options):
        print(f"{chr(65 + i)}) {option}")
    start_time = time.time()

    # Create and start the input reading thread
    input_thread = threading.Thread(target=read_response)
    input_thread.start()

    # Wait for the input thread to complete or timeout
    input_thread.join()

    # Check if participant entered a response
    response = participant_response if participant_response is not None else None

    response_time = None if response is None else time.time() - start_time

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
        print(f"Response Time: {response_time:.2f} seconds") if response_time is not None else print("Response Time: N/A")
        print(f"Correct: {correct}")
        print("------------------")

# Stroop experiment questions and answers
questions = [
    (colored(f"What color is the word written in? RED", "blue"),
     [colored("Red", "red"), colored("Blue", "blue"), colored("Green", "green"), colored("Yellow", "yellow")], "B"),
    (colored(f"What color is the word written in? BLUE", "green"),
     [colored("Red", "red"), colored("Yellow", "yellow"), colored("Green", "green"), colored("Blue", "blue")], "C"),
    (colored(f"What color is the word written in? GREEN", "yellow"),
     [colored("Yellow", "yellow"), colored("Green", "green"), colored("Red", "red"), colored("Blue", "blue")], "A"),
    (colored(f"What color is the word written in? YELLOW", "blue"),
     [colored("Green", "green"), colored("Blue", "blue"), colored("Yellow", "yellow"), colored("Red", "red")], "B"),
    (colored(f"What color is the word written in? RED", "yellow"),
     [colored("Red", "red"), colored("Blue", "blue"), colored("Green", "green"), colored("Yellow", "yellow")], "D"),
    (colored(f"What color is the word written in? PURPLE", "magenta"),
     [colored("Yellow", "yellow"), colored("Grey", "grey"), colored("Black", "black"), colored("Magenta", "magenta")], "D"),
    (colored(f"What color is the word written in? ORANGE", "cyan"),
     [colored("Grey", "grey"), colored("Red", "red"), colored("Cyan", "cyan"), colored("White", "white")], "C")
    # Add more questions here
]



questions_1 = [
    (colored(f"What color is the word written in? RED", "blue"),
     [colored("Red", "red"), colored("Blue", "blue"), colored("Green", "green"), colored("Yellow", "yellow")], "B"),
    (colored(f"What color is the word written in? BLUE", "green"),
     [colored("Red", "red"), colored("Yellow", "yellow"), colored("Green", "green"), colored("Blue", "blue")], "C"),
    (colored(f"What color is the word written in? GREEN", "yellow"),
     [colored("Yellow", "yellow"), colored("Green", "green"), colored("Red", "red"), colored("Blue", "blue")], "A"),
    (colored(f"What color is the word written in? YELLOW", "blue"),
     [colored("Green", "green"), colored("Blue", "blue"), colored("Yellow", "yellow"), colored("Red", "red")], "B"),
    (colored(f"What color is the word written in? RED", "yellow"),
     [colored("Red", "red"), colored("Blue", "blue"), colored("Green", "green"), colored("Yellow", "yellow")], "D"),
    (colored(f"What color is the word written in? PURPLE", "magenta"),
     [colored("Yellow", "yellow"), colored("Grey", "grey"), colored("Black", "black"), colored("Magenta", "magenta")], "D"),
    (colored(f"What color is the word written in? ORANGE", "cyan"),
     [colored("Grey", "grey"), colored("Red", "red"), colored("Cyan", "cyan"), colored("White", "white")], "C"),
    (colored(f"What is the color word written in? GREEN", "red"),
     [colored("Red", "red"), colored("Blue", "blue"), colored("Green", "green"), colored("Yellow", "yellow")], "C"),
    (colored(f"What is the color word written in? BLUE", "green"),
     [colored("Red", "red"), colored("Blue", "blue"), colored("Green", "green"), colored("Yellow", "yellow")], "B"),
    (colored(f"What is the color word written in? YELLOW", "blue"),
     [colored("Red", "red"), colored("Blue", "blue"), colored("Green", "green"), colored("Yellow", "yellow")], "D")
    
]


# experiment choice
experiment_choice = input("Enter experiment choice (1 for Stress, 2 for Relaxed): ")

# Participant details
participant_name = input("Enter your name: ")

# # Perform song timing
# response_time_1, response_time_2 = perform_song_timing()


if experiment_choice == "1":

    results = []
    # for i in range(len(questions)):
    # Perform song timing
    response_time_1, response_time_2 = perform_song_timing()
    i=1
    prev_random_number = None

    while(i<=10):
            
        if random.random() < 0.7:
            # Stroop experiment question
            random_number = random.randint(0, len(questions_1) - 1)
            while random_number == prev_random_number:
                random_number = random.randint(0, len(questions_1) - 1)
            prev_random_number = random_number
            question, options, correct_answer = questions_1[random_number]
            response, response_time = record_response(question, options)
            correct = response == correct_answer
            results.append((question, response, response_time, correct))
            i+=1
        elif i<=10:
            # Perform song timing
            response_time_1, response_time_2 = perform_song_timing()
            results.append(("Song Timing", "N/A", response_time_2+response_time_1, False))
        else:
            exit
        print("\n")





    # Function to save results as a text file
    def save_results_as_text(results, filename):
        with open(filename, mode="w") as file:
            for result in results:
                question = result[0]
                response = result[1]
                response_time = result[2]
                correct = result[3]

                file.write(f"Question: {question}\n")
                file.write(f"Response: {response}\n")
                file.write(f"Response Time: {response_time:.2f} seconds\n") if response_time is not None else file.write("Response Time: N/A\n")
                file.write(f"Correct: {correct}\n")
                file.write("------------------\n")



    # Display the results
    display_results(results)
    file_name = "result_"+str(participant_name)+str(experiment_choice)
    save_results_as_text(results, filename=file_name)            


elif experiment_choice == "2":
    results = []

    i = 1
    j = 1

    while i <= 7:
        question_index = random.randint(0, len(questions_1) - 1)
        if random.random() < 0.7:
            selected_questions = random.sample(questions_1, 10)
            for question, options, correct_answer in selected_questions:
                if j <= 15:
                    question_text = f"Question {j}: {question}"  # Add the question number to the question text
                    response, response_time = record_response(question_text, options)
                    correct = response == correct_answer
                    results.append((question_text, response, response_time, correct))
                    j += 1
                else:
                    exit
            i += 1
        else:
            # Perform song timing
            pass
        i += 1
        print("\n")




    # Function to save results as a text file
    def save_results_as_text(results, filename):
        with open(filename, mode="w") as file:
            for result in results:
                question = result[0]
                response = result[1]
                response_time = result[2]
                correct = result[3]

                file.write(f"Question: {question}\n")
                file.write(f"Response: {response}\n")
                file.write(f"Response Time: {response_time:.2f} seconds\n") if response_time is not None else file.write("Response Time: N/A\n")
                file.write(f"Correct: {correct}\n")
                file.write("------------------\n")



    # Display the results
    display_results(results)
    file_name = "result_"+str(participant_name)+str(experiment_choice)+str(".txt")
    save_results_as_text(results, filename=file_name)