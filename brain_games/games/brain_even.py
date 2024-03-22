from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise 
answer "no".'


def generate_question() -> str:
    '''Generate random integer number and return it
    as a string'''
    return str(randint(1, 100))


def get_correct_answer(question: str) -> str:
    '''Take integer number as a string and return string 
'yes'
    if the number is even, otherwise string 'no' if odd'''
    return 'no' if int(question) % 2 else 'yes'
