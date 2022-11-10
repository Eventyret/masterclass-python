import random

choices = ["Rock","Paper","Scissors"]

def loop_for_choices():
    
    for i in range(len(choices)):
        print(choices[i])
        

loop_for_choices()

def computer_choice():
    choices = ["rock", "paper", "scissors"]
    computer_option = choices[random.randint(0, 2)]
    return computer_option


print(computer_choice())

#User input # Aron & Adan

#Computer choice # Gabor Neil



