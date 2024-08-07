import random


DESCRIPTION = 'What number is missing in the progression?'
SIZE_PROGRESSION = 10
MIN_START = 1
MAX_START = 100
MIN_STEP = 2
MAX_STEP = 5


def generate_progression():
    start = random.randint(1, 100)
    rule = random.randint(2, 5)
    progression = [start]
    for i in range(SIZE_PROGRESSION):
        progression.append(progression[i] + rule)
    return progression


def generate_round_data():
    progression = generate_progression()
    random_index = random.randint(0, SIZE_PROGRESSION - 1)
    right = progression[random_index]
    progression[random_index] = '..'
    question = list(map(str, progression))
    return ' '.join(question), str(right)
