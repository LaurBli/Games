import random
from random import randint

pick = ['Rock', 'Paper', 'Scissors']

computer = pick[randint(0, 1)]

player = False
player_score = 0
computer_score = 0
games = -1
print('If you want to end the game, type "End"')
while player == False:
    choice = input('Rock,Paper or Scissors?->')
    games += 1
    if choice == computer:
        print("It's a tie")
        computer_score += 1
        player_score += 1
    elif choice == 'Rock' and computer == 'Scissors':
        print(f'{choice} breaks {computer}. You win!')
        player_score += 1
    elif choice == 'Rock' and computer == 'Paper':
        print(f'{computer} covers {choice}. You lost!')
        computer_score += 1
    elif choice == 'Paper' and computer == 'Rock':
        print(f'{choice} covers {computer}. You win!')
        player_score += 1
    elif choice == 'Paper' and computer == 'Scissors':
        print(f'{computer} cuts {choice}. You lost!')
        computer_score += 1
    elif choice == 'Scissors' and computer == 'Rock':
        print(f'{computer} breaks {choice}. You lost!')
        computer_score += 1
    elif choice == 'Scissors' and computer == 'Paper':
        print(f'{choice} cuts {computer}. You win!')
        player_score += 1
    elif choice == 'End':
        if player_score > computer_score:
            print(f'You played {games} games\nYour Score : {player_score}\nComputer score: {computer_score}\nYOU WIN!')
            break
        elif player_score == computer_score:
            print(f'You played {games} games\nYour Score : {player_score}\nComputer score: {computer_score}\nTIE')
            break
        else:
            print(f'You played {games} games\nYour Score : {player_score}\nComputer score: {computer_score}\nYOU LOST!')
            break
    else:
        print('Please check your spelling and try again')
        games-=1

player = False
computer = pick[randint(0, 1)]
