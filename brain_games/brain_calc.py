from random import randint
import prompt

DESCRIPTION = "What is the result of the expression?"

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    def generate_question():
        """Generate a math question."""
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        operator = randint(1, 3)
        if operator == 1:
            question = f"{num1} + {num2}"
            correct_answer = num1 + num2
        elif operator == 2:
            question = f"{num1} - {num2}"
            correct_answer = num1 - num2
        else:
            question = f"{num1} * {num2}"
            correct_answer = num1 * num2
        return question, str(correct_answer)

    for _ in range(3):
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        
        if user_answer != correct_answer:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(user_answer, correct_answer))
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()

