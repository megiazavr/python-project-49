from random import randint


game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round_data():
    value = random.randint(1, 10)
    question = f'{value}'
    right = value % 2 and 'no' or 'yes'
    return question, right
