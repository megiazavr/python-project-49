from random import randint


game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer() -> tuple[int, str]:
    number = randint(0, 25)
    right_answer = 'yes' if number % 2 == 0 else 'no'
    return number, right_answer

def is_even(number: int) -> bool:
    return number % 2 == 0
