#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from random import randint
from art import logo
from replit import clear

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to be called if the player still wanted to play again
def play_again():
  play_again = input("Type 'y' if you want to play again and 'n' if not. ")
  if play_again == 'y':
    clear()
    game()
  else:
    return

# Function to check the user's guess against the actual answer
def check_answer(guess, answer, turns):
  """Checks the answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too High! ")
    return turns - 1
  elif guess < answer:
    print("Too Low! ")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer} !")
    play_again()


# Function to set difficulty
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

# Function that will run the whole game
def game():
  print(logo)
  # Choosing a random number between 1 and 100
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Psst, the correct asnwer is {answer}")
  
  turns = set_difficulty()
  
  
  # Repeat the guessing game
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    
    # Let a user guess a number
    guess = int(input("Make a guess: "))
    
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses! You loose!")
      play_again()
    elif guess != answer:
      print("Guess again. ")


game()