import itertools

from random import choice

game_choices = ['rock', 'paper', 'scissors']

correct_count = 0
prev_choice = None
prev_prev_choice = None
prev_prev_prev_choice = None
combinations = list(itertools.product(game_choices, repeat=4))

combination_history = {combination: 0 for combination in combinations}

for i in range(7):
    computer_choice = choice(game_choices)
    user_choice = input('Enter your choice: ')
    print(f'Computer chose => {computer_choice}')

    if computer_choice == user_choice:
        correct_count += 1
    if i > 2:
        combination_history[(prev_prev_prev_choice, prev_prev_choice, prev_choice, user_choice)] += 1

    prev_prev_prev_choice = prev_prev_choice
    prev_prev_choice = prev_choice
    prev_choice = user_choice

for i in range(7):
    prediction = None
    user_choice = input('Enter your choice: ')
    print(f'Computer chose => {computer_choice}')

    if i > 2:
        if combination_history[(prev_prev_prev_choice, prev_prev_choice, prev_choice, 'rock')] > combination_history[(prev_prev_prev_choice, prev_prev_choice, prev_choice, 'paper')]:
            prediction = 'rock'
        else:
            prediction = 'paper'

        if combination_history[(prev_prev_prev_choice, prev_prev_choice, prev_choice, 'rock')] > combination_history[(prev_prev_prev_choice, prev_prev_choice, prev_choice, 'scissors')]:
            prediction = 'rock'
        else:
            prediction = 'scissors'

        if combination_history[(prev_prev_prev_choice, prev_prev_choice, prev_choice, 'paper')] > combination_history[(prev_prev_prev_choice, prev_prev_choice, prev_choice, 'rock')]:
            prediction = 'paper'
        else:
            prediction = 'rock'

        if combination_history[(prev_prev_prev_choice, prev_prev_choice, prev_choice, 'paper')] > combination_history[(prev_prev_prev_choice, prev_prev_choice, prev_choice, 'scissors')]:
            prediction = 'paper'
        else:
            prediction = 'scissors'

        if combination_history[(prev_prev_prev_choice, prev_prev_choice, prev_choice, 'scissors')] > combination_history[(prev_prev_prev_choice, prev_prev_choice, prev_choice, 'rock')]:
            prediction = 'scissors'
        else:
            prediction = 'rock'

        if combination_history[(prev_prev_prev_choice, prev_prev_choice, prev_choice, 'scissors')] > combination_history[(prev_prev_prev_choice, prev_prev_choice, prev_choice, 'paper')]:
            prediction = 'scissors'
        else:
            prediction = 'paper'
    if computer_choice == user_choice:
        correct_count += 1
    combination_history[(prev_prev_prev_choice, prev_prev_choice, prev_choice, user_choice)] += 1

    prev_prev_prev_choice = prev_prev_choice
    prev_prev_choice = prev_choice
    prev_choice = user_choice

print(f"Computer wins : {correct_count} times.")
