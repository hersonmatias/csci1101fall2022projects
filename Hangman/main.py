import re

# Getting the answer.
answer = "What's Up, Doc?"

answer = answer.upper()

# Game setup.
num_of_incorrect_guesses = 5

answer_guessed = []

for current_answer_character in answer:
    if re.search("^[A-Z]$", current_answer_character):
        answer_guessed.append(False)
    else:
        answer_guessed.append(True)

#game logic
