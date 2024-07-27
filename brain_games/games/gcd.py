import random
import math

DESCRIPTION  = 'Find the greatest common divisor of given numbers.'

def generate_round_data():
    value1 = random.randint(1, 10)
    value2 = random.randint(1, 10)
    question = f'Question: {value1} {value2}'
    right = value % 2 and 'no' or 'yes'
    return question, right
