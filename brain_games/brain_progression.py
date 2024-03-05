import random
import prompt

DESCRIPTION = 'What number is missing in the progression?'

def generate_progression():
    """Generate arithmetic progression with a missing number."""
    start = random.randint(1, 20)
    step = random.randint(1, 5)
    length = random.randint(5, 10)
    progression = [str(start + i * step) for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(progression)
    return question, correct_answer

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(DESCRIPTION)

    for _ in range(3):
        question, correct_answer = generate_progression()
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

