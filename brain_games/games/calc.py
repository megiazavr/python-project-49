from operator import add, sub, mul
from random import randint
import random


game_rule = 'What is the result of the expression?'


def get_question_and_answer() -> tuple[str, int]:
    num1, num2 = randint(1, 25), randint(1, 25)
    operators_dictionary = {
        "+": add(num1, num2),
        "-": sub(num1, num2),
        "*": mul(num1, num2)
    }
    operator_ = random.choice(list(operators_dictionary.keys()))
    right_answer = operators_dictionary[operator_]
    question = f'{num1} {operator_} {num2}'
    return question, right_answer
