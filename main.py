import random


def computer_choice():
    choices = ["rock", "paper", "scissors"]
    computer_option = choices[random.randint(0, 2)]
    return computer_option


print(computer_choice())
