from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. 
Otherwise answer "no".'


def generate_question() -> str:
    '''Generate random integer number and
    return it as a string object'''
    return str(randint(1, 99))


def get_correct_answer(question: int) -> str:
    '''Take integer number as a string and return "yes"
    if number is prime or "no" if not'''
    number = int(question)
    for i in range(2, int(number // 2) + 1):
        if number % i == 0:
            return 'no'
    return 'no' if number == 1 else 'yes'
