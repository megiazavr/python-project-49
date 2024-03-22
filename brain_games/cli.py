#!/usr/bin/env python

import prompt

def welcome_user() -> str:
    "Greet user, ask his/her name and return it"
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def say_game_over(user: str) -> str:
    "Say goodbye to user when the answer was incorrect"
    print(f"Let's try again, {user}!")


def say_well_done(user: str) -> str:
    "Say goodbye to user when all answers was correct"
    print(f"Congratulations, {user}!")


def get_user_answer():
    "Ask user to input answer to the question"
    return input('Your answer: ')

if __name__ == '__main__':
	welcome_user()
