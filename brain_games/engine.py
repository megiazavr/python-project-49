import prompt
from brain_games.constants import ROUNDS_COUNT

def play(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    for _ in range(ROUNDS_COUNT):
        question, right = game.generate_round_data()
        print(f'Question: {question}')
        answ = prompt.string('Your answer: ')
        if answ != right:
            print(f"'{answ}' is wrong answer ;(. Correct answer was '{right}'.")
            print(f"Let's try again, {name}!")
            break
        print('Correct!')
    else:
        print(f'Congratulations, {name}!')
