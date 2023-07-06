import time

def perform_song_timing():
    # Question 1: Time to prepare to sing a song
    print("This is the time to prepare to sing a song.")
    start_time = time.time()
    for i in range(5, 0, -1):
        print(f"{i}..", end='', flush=True)
        time.sleep(1)
    end_time = time.time()
    response_time_1 = end_time - start_time
    print("\n")

    # Question 2: Prompt to start singing the song
    print("Please start singing the song.")
    start_time = time.time()
    for i in range(5, 0, -1):
        print(f"{i}..", end='', flush=True)
        time.sleep(1)
    end_time = time.time()
    response_time_2 = end_time - start_time
    print("\n")

    return response_time_1, response_time_2
