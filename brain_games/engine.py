import brain_games.cli


ANSWERS_TO_COMPLETE = 3


def run_game(game_module, cli_module=brain_games.cli) -> None:
    '''Take the game resources module and run the game'''
    user = cli_module.welcome_user()
    print(game_module.DESCRIPTION)
    answers_left = ANSWERS_TO_COMPLETE  # the required number of correct answers
    while answers_left > 0:
        question = game_module.generate_question()
        print(f'Question: {question}')
        correct_answer = game_module.get_correct_answer(question)
        user_answer = cli_module.get_user_answer()
        if user_answer == correct_answer:
            answers_left -= 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{correct_answer}'.")
            cli_module.say_game_over(user)
            break
    else:
        cli_module.say_well_done(user)
