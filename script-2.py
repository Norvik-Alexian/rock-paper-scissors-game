import itertools

from random import choice

game_choices = ['rock', 'paper', 'scissors']


class Game:
    def __init__(self):
        self.correct_count = 0
        self.prev_choice = None
        self.prev_prev_choice = None
        self.prev_prev_prev_choice = None
        self.prediction = None

    def collecting_history(self):
        combinations = list(itertools.product(game_choices, repeat=4))
        combination_history = {combination: 0 for combination in combinations}

        for i in range(7):
            computer_choice = choice(game_choices)
            user_choice = input('Enter your choice: ')
            print(f'Computer chose => {computer_choice}')

            if computer_choice == user_choice:
                self.correct_count += 1
            if i > 2:
                combination_history[(self.prev_prev_prev_choice, self.prev_prev_choice, self.prev_choice, user_choice)] += 1

            self.prev_prev_prev_choice = self.prev_prev_choice
            self.prev_prev_choice = self.prev_choice
            self.prev_choice = user_choice

        return combination_history, computer_choice

    def guess_possiblity(self):
        computer_choice = self.collecting_history()[1]
        combination_history = self.collecting_history()[0]

        for i in range(7):
            user_choice = input('Enter your choice: ')
            print(f'Computer chose => {computer_choice}')

            if i > 2:
                if combination_history[(self.prev_prev_prev_choice, self.prev_prev_choice, self.prev_choice, 'rock')] > \
                        combination_history[(self.prev_prev_prev_choice, self.prev_prev_choice, self.prev_choice, 'paper')]:
                    self.prediction = 'rock'
                else:
                    self.prediction = 'paper'

                if combination_history[(self.prev_prev_prev_choice, self.prev_prev_choice, self.prev_choice, 'rock')] > \
                        combination_history[(self.prev_prev_prev_choice, self.prev_prev_choice, self.prev_choice, 'scissors')]:
                    self.prediction = 'rock'
                else:
                    self.prediction = 'scissors'

                if combination_history[(self.prev_prev_prev_choice, self.prev_prev_choice, self.prev_choice, 'paper')] > \
                        combination_history[(self.prev_prev_prev_choice, self.prev_prev_choice, self.prev_choice, 'rock')]:
                    self.prediction = 'paper'
                else:
                    self.prediction = 'rock'

                if combination_history[(self.prev_prev_prev_choice, self.prev_prev_choice, self.prev_choice, 'paper')] > \
                        combination_history[(self.prev_prev_prev_choice, self.prev_prev_choice, self.prev_choice, 'scissors')]:
                    self.prediction = 'paper'
                else:
                    self.prediction = 'scissors'

                if combination_history[(self.prev_prev_prev_choice, self.prev_prev_choice, self.prev_choice, 'scissors')] > \
                        combination_history[(self.prev_prev_prev_choice, self.prev_prev_choice, self.prev_choice, 'rock')]:
                    self.prediction = 'scissors'
                else:
                    self.prediction = 'rock'

                if combination_history[(self.prev_prev_prev_choice, self.prev_prev_choice, self.prev_choice, 'scissors')] > \
                        combination_history[(self.prev_prev_prev_choice, self.prev_prev_choice, self.prev_choice, 'paper')]:
                    self.prediction = 'scissors'
                else:
                    self.prediction = 'paper'
            if computer_choice == user_choice:
                self.correct_count += 1
            combination_history[(self.prev_prev_prev_choice, self.prev_prev_choice, self.prev_choice, user_choice)] += 1

            self.prev_prev_prev_choice = self.prev_prev_choice
            self.prev_prev_choice = self.prev_choice
            self.prev_choice = user_choice

        print(f"Computer wins: {self.correct_count} times.")


game = Game()
game.guess_possiblity()