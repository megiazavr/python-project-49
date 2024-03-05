import random
import math
import prompt

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = str(gcd(num1, num2))
    return question, correct_answer

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(DESCRIPTION)

    for _ in range(3):
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()

