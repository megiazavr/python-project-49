import random
import math

DESCRIPTION  = 'Find the greatest common divisor of given numbers.'

def generate_round_data():
    value = random.randint(1, 10)
    question = f'{value}'
    right = value % 2 and 'no' or 'yes'
    return question, right
