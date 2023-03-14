#A rock paper scissors game
#Rock beats scissors, scissors beat paper, and paper beats rock.
#The computer generates its options while the user enters r, p, s or q
#the program keeps count of wins for both user and computer and siplays them at the end
import random

def play():
    user_wins = 0
    comp_wins = 0
    options = ['r', 'p', 's']

    while True:
        comp_choice = random.choice(['r', 'p', 's'])
        
        user_input = input("Enter r for rock, p for paper, s for scissors and q to quit: ").lower()
        
        if user_input == 'q':
            break
        if user_input not in options:
            continue
        print(f'Computer chose: {comp_choice}')
        
        
        if comp_choice == user_input:
            print("It's a tie!")
        
        
        elif is_win(user_input, comp_choice):
            print("You win!")
            user_wins += 1

        elif not is_win(user_input, comp_choice):
            print("You lose!")
            comp_wins += 1
    print(f"You won {user_wins} times and computer won {comp_wins} times")
    if user_wins > comp_wins:
        print("Congratulations! You win!")
    elif user_wins == comp_wins:
        print("It's a tie!")
    else:
        print("You lose!")


def is_win(user, comp):
    if user == 'p' and comp == 'r' or user == 's' and comp == 'p' or user == 'r' and comp == 's':
        return True
    

play()
