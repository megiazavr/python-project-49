from random import randint
import prompt

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    def main_num():
        min_num = 1
        max_num = 99
        number = randint(min_num, max_num)
        question = str(number)

        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        print("Answer 'yes' if the number is even, otherwise answer 'no'.")
        return question, correct_answer

    for _ in range(3):  # Позволим пользователю три попытки
        question, correct_answer = main_num()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")

def generate_question() -> str:
    '''Generate random integer number and return it
    as a string'''
    return str(randint(1, 100))


def get_correct_answer(question: str) -> str:
    '''Take integer number as a string and return string 'yes'
    if the number is even, otherwise string 'no' if odd'''
    return 'no' if int(question) % 2 else 'yes'

if __name__ == "__main__":
    main()
