from random import randint, randrange


DESCRIPTION = 'What number is missing in the progression?'


def generate_question() -> str:
    '''Generate arithmetic progression with one lost number
    and return it as a string'''
    start, step, length = randint(1, 50), randint(1, 10), 
randint(5, 10)
    progression = list(range(start, start + step * length, 
step))
    progression[randrange(length)] = '..'
    return ' '.join(str(x) for x in progression)


def get_correct_answer(question: str) -> str:
    '''Take ariphmetic progression of integer numbers 
splitted by
    spaces, find and return the lost number as a string'''
    numbers = question.split()
    i = numbers.index('..')
    if i >= 2:
        lost_num = 2 * int(numbers[i - 1]) - int(numbers[i - 
2])
    else:
        lost_num = 2 * int(numbers[i + 1]) - int(numbers[i + 
2])
    return str(lost_num)
