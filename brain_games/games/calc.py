import random


DESCRIPTION = 'What is the result of the expression?'


def generate_round_data():
    number_a = random.randint(1, 10)
    number_b = random.randint(1, 10)
    operator = random.choice('+-*')
    match operator:
        case '*':
            right = number_a * number_b
            question = f'{number_a} * {number_b}'
        case '-':
            right = number_a - number_b
            question = f'{number_a} - {number_b}'
        case '+':
            right = number_a + number_b
            question = f'{number_a} + {number_b}'
    return question, str(right)
