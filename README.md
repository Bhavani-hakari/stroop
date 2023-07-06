# README

This script is designed to conduct a Stroop experiment where participants are presented with color-related questions and their responses and response times are recorded. The experiment offers two modes: a stress mode and a relaxed mode.

## Dependencies

The script requires the following dependencies:

- `select`: Used for reading participant responses.
- `sys`: Used for standard input and output operations.
- `time`: Used for measuring response times.
- `threading`: Used for running input reading in a separate thread.
- `termcolor`: Used for displaying colored text.
- `song_timing`: A custom module for measuring song timing. 

Please make sure to have these dependencies installed before running the script.

## Usage

1. Run the script by executing the Python file.
2. When prompted, enter the experiment choice:
   - Enter `1` for the stress mode.
   - Enter `2` for the relaxed mode.
3. Enter your name when prompted to provide participant details.
4. Follow the instructions and respond accordingly to the presented questions.

## Stress Mode

In the stress mode (choice `1`), the script will perform the following steps:

1. Measure song timing: The script will measure the response time for two songs using the `perform_song_timing` function (implementation not provided).

2. Stroop Experiment Questions: The script will present a total of 10 randomly selected Stroop experiment questions. The questions will ask about the color of the displayed words, and the participant needs to choose the correct color from the provided options. The response time for each question will be recorded.

3. Song Timing Task: After each Stroop question, there is a chance that the script will require the participant to sing a song. This is intended to induce stress. The participant should follow the instructions and sing the song. The response time for this task will also be recorded.

4. Display Results: Once the experiment is completed, the script will display the results, including each question, the participant's response, the response time, and whether the response was correct.

5. Save Results: The results will be saved in a text file named "result_participantname1.txt", where "participantname" is the name entered by the participant.

## Relaxed Mode

In the relaxed mode (choice `2`), the script will perform the following steps:

1. Stroop Experiment Questions: The script will present a total of 15 randomly selected Stroop experiment questions. The questions will ask about the color of the displayed words, and the participant needs to choose the correct color from the provided options. The response time for each question will be recorded.

2. Display Results: Once the experiment is completed, the script will display the results, including each question, the participant's response, the response time, and whether the response was correct.

3. Save Results: The results will be saved in a text file named "result_participantname2.txt", where "participantname" is the name entered by the participant.

## Note

Feel free to modify the code or experiment questions to suit your needs.
