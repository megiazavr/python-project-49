from random import randint


game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer() -> tuple[int, str]:
    number = randint(2, 100)
    right_answer = 'yes' if is_prime(number) else 'no'
    return number, right_answer


def is_prime(number: int) -> bool:
    for divider in range(2, (number // 2) + 1):
        if number % divider == 0:
            return False
    return True
