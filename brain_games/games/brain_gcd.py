from random import randint
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given 
numbers.'


def generate_question() -> str:
    '''Generate 2 random integers and return it
    splitted with space as a string'''
    num_1, num_2 = randint(1, 100), randint(1, 100)
    return f'{num_1} {num_2}'


def get_correct_answer(question: str) -> str:
    '''Take two integers as a string and return their
    greatest common divisor as a string'''
    num_1, num_2 = map(int, question.split())
    return str(gcd(num_1, num_2))
