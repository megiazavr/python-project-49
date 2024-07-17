from random import randint

game_rule = 'What number is missing in the progression?'

from random import randint

GAME_RULE = 'What number is missing in the progression?'
MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 11
MIN_START = 1
MAX_START = 20
MIN_STEP = 2
MAX_STEP = 6

def get_question_and_answer() -> tuple[str, str]:
    progression = generate_progression()
    question, right_answer = hide_element_in_progression(progression)
    return question, right_answer

def generate_progression() -> list[int]:
    length = randint(5, 11)
    start = randint(1, 20)
    step = randint(2, 6)
    stop = start + (length * step)
    progression = list(range(start, stop, step))
    return progression

def hide_element_in_progression(progression: list[int]) -> tuple[str, str]:
    hide_char_index = randint(0, len(progression) - 1)
    right_answer = str(progression[hide_char_index])
    progression[hide_char_index] = '..'
    question = " ".join(map(str, progression))
    return question, right_answer

