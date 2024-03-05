from random import randint
from cli import welcome_user
from brain_games import main

from random import randint
import prompt

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def display_rules():
    """Display the rules of the game."""
    print("Welcome to the Brain Even Games!")
    print(DESCRIPTION)


def make_question_and_correct_answer():
    """Generate a question and its correct answer."""
    min_number = 1
    max_number = 99
    number = randint(min_number, max_number)
    question = str(number)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return question, correct_answer


def main():
    display_rules()
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    for _ in range(3):  # Allow the user three attempts
        question, correct_answer = make_question_and_correct_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer.lower() == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was 
'{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()

