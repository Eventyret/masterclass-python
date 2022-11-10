import random


def computer_choice():
    choices = ["rock", "paper", "scissors"]
    computer_option = choices[random.randint(0, 2)]
    return computer_option


print(computer_choice())

def get_answers(user_input):
    who_beats_who = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    losing_choice = who_beats_who[user_input]
    # key = user_input
    return losing_choice
    print(losing_choice)
#User input # Aron & Adan

choices = ["rock","paper","scissors"]
def take_input():
    user_input = input("type rock, paper or scissors")
    if user_input == 'rock' || 'paper' || 'scissors':
        return user_input
    else :
        print('error: choice must be either rock, paper or scissors')

get_answers()

def judgement(user_input, computer_option):
    if user_input == computer_option:
        print('draw') 
    elif losing_choice == True:
        print('user wins')
    else:
        print('computer wins')
