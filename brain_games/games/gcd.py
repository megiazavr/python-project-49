import random
import math

DESCRIPTION  = 'Find the greatest common divisor of given numbers.'

def generate_round_data():
    value1 = random.randint(1, 100)
    value2 = random.randint(1, 100)
    question = f'Question: {value1} {value2}'
    correct_answer = str(math.gcd(value1, value2))
    return question, right
