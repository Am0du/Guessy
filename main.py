#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from replit import clear
from art import logo

def check_guess(comp_guess, user_guess, user_name):
    """Checks if the player guess the right number"""
    if user_guess == comp_guess:
        return f"Correct!!! The computer guessed {comp_guess}, {user_name} wins"
    elif user_guess > comp_guess:
        return "Too high"
    elif user_guess < comp_guess:
        return "Too low"


def game_level(user_level):
    """Checks the level of difficult the player inputed"""
    if user_level == 'hard':
        player_life = 5
        return player_life
    elif user_level == 'easy':
        player_life = 10
        return player_life
        
def game_logo():
    clear()
    return print(logo)
    
    
    

print(f"{logo}\nWelcome to the Number Guessing game!\nI'm thinking of a number between 1 and 100")
user_name = input("What's your name: ")
diff_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

comp_ = random.randint(1, 100)

if game_level(diff_level):
    player_life = game_level(diff_level)
    guess = True
    while guess is True:
        print(f"You've have {player_life} life remaining to get the answer")
        user_ = int(input("Make a guess: "))
        
        print(check_guess(comp_, user_, user_name))
        player_life -= 1
           
        user_choice = input("Do you want to stop, Type 'yes' to stop and 'no' to continue: ").lower()
        if player_life == 0 or user_ == comp_ or user_choice == 'yes':
            guess = False
        game_logo()

    if player_life == 0:
        game_logo()
        print("you've used up your life\nGame over!!!!!")
    elif user_choice =='yes':
        game_logo()
        print(f"Your guess is {check_guess(comp_, user_, user_name)}")
        


        
else:
    print("Invalid input")