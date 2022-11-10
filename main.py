import random


def computer_choice():
    choices = ["rock", "paper", "scissors"]
    computer_option = choices[random.randint(0, 2)]
    return computer_option


def get_answers(user_input):
    who_beats_who = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    losing_choice = who_beats_who[user_input]
    # key = user_input
    return losing_choice


def take_input():
    user_input = input("type rock, paper or scissors")
    if user_input == 'rock' or 'paper' or 'scissors':
        judgement(user_input, computer_choice())
    else:
        print('error: choice must be either rock, paper or scissors')


def judgement(user_input, computer_option):
    if user_input == computer_option:
        print('draw')
    elif losing_choice == computer_option:
        print('user wins')
    else:
        print('computer wins')


take_input()