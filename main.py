import random


def computer_choice():
    choices = ["rock", "paper", "scissors"]
    computer_option = choices[random.randint(0, 2)]
    return computer_option


print(computer_choice())

#User input # Aron & Adan

choices = ["rock","paper","scissors"]
def take_input():
    user_input = input("type rock, paper or scissors")
    if user_input == 'rock' || 'paper' || 'scissors':
        return user_input
    else :
        print('error: choice must be either rock, paper or scissors')


