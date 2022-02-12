from random import choice

game_choices = ['rock', 'paper', 'scissors']

for _ in range(5):
    user_choice = input('Enter your choice: ')
    computer_choice = choice(game_choices)
    print(f'You chose: {user_choice}\nComputer chose: {computer_choice}')

    if user_choice == computer_choice:
        print(f"both playered chose {user_choice}, it's tie\n")
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print('paper covers rock, you win!\n')
        else:
            print('scissors cuts paper, you lose!\n')
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            print('paper covers rock, you lose!\n')
        else:
            print('rock beats scissors, you win!\n')
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            print('rock beats scissors, you lose!\n')
        else:
            print('scissors cuts paper, you win!\n')
