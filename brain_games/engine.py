def greet_user_and_get_user_name(game_rule: str) -> str:
    print('Welcome to the Brain Games!')
    user_name = prompt.string("May I have your name? ")
    print(f'Hello, {user_name}!')
    print(game_rule)
    return user_name


def show_question_get_user_answer(question: str) -> str:
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    return answer


def start_game(game: ModuleType) -> None:
    game_rule = game.game_rule
    user_name = greet_user_and_get_user_name(game_rule)
    for _ in range(ROUNDS):
        question, right_answer = game.get_question_and_answer()
        user_answer = show_question_get_user_answer(question)
        if user_answer == str(right_answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')
