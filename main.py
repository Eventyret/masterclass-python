def get_answers(key):
    who_beats_who = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    loses = who_beats_who[key]
    return loser
    print(loser)

get_answers('rock')

if user_choice == computer_choice:
    print('draw') 
elif loses == computer_choice:
    print('user wins')
else:
    print('computer wins')
