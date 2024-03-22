from random import randint, choice
from operator import add, sub, mul


DESCRIPTION = 'What is the result of the expression?'
OPERATORS = {'+': add, '-': sub, '*': mul}


def generate_question() -> str:
    '''Generate random arithmetic operation between
    two integers and return it as a string'''
    num_1, num_2 = randint(1, 100), randint(1, 100)
    operation = choice(list(OPERATORS))
    return f'{num_1} {operation} {num_2}'


def get_correct_answer(question: str) -> str:
    '''Take an arithmetic operation string and return
    the right solution number as a string'''
    num_1, op_char, num_2 = question.split()
    result = OPERATORS[op_char](int(num_1), int(num_2))
    return str(result)
