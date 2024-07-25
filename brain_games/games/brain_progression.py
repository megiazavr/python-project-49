from random import randint

from random import randint

GAME_RULE = 'What number is missing in the progression?'
MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 11
MIN_START = 1
MAX_START = 20
MIN_STEP = 2
MAX_STEP = 6

def get_question_and_answer() -> tuple[str, str]:
    length = randint(MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
    start = randint(MIN_START, MAX_START)
    step = randint(MIN_STEP, MAX_STEP)
    progression = generate_progression(start, step, length)
    hide_char_index = randint(0, len(progression) - 1)
    question, right_answer = hide_element_in_progression(progression, 
hide_char_index)
    return question, right_answer
 
generate_progression(start: int, step: int, length: int) -> list[int]:
    stop = start + (length * step)
    progression = list(range(start, stop, step))
    return progression

def hide_element_in_progression(progression: list[int]) -> tuple[str, str]:
    right_answer = str(progression[hide_char_index])
    progression[hide_char_index] = '..'
    question = " ".join(map(str, progression))
    return question, right_answer

