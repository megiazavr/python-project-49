import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5 + 1)):
        if not (number % i):
            return False
    return True


def generate_round_data():
    number = random.randint(1, 10)
    right = is_prime(number) and 'yes' or 'no'
    question = number
    return question, str(right)
