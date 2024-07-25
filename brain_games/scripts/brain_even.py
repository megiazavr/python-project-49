from brain_games.games.even import get_question_and_answer, game_rule
from brain_games.engine import play_game


def main():
    return play_game(get_question_and_answer, game_rule)


if __name__ == '__main__':
    main()
