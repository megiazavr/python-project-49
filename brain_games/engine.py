from types import ModuleType
import prompt

ROUNDS = 3

def start_game(game: ModuleType) -> None:
    print('Welcome to the Brain Games!')
    user_name = prompt.string("May I have your name? ")
    print(f'Hello, {user_name}!')
    print(game.game_rule)
    
    for _ in range(ROUNDS):
        question, right_answer = game.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        
        if user_answer == str(right_answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')

