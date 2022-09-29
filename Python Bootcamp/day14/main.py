from art import logo, vs
from game_data import data
import random
from replit import clear

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Takes the account into printable format: name, description and country."""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a/an {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  """ Take the user guess and follower counts and returns if they got it right."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
    
  # Display art
  print(logo)
  score = 0
  continue_game = True
  account_a = get_random_account()
  account_b = get_random_account()
  
  # Make the game repeatable
  while continue_game:  
    account_a = account_b
    account_b = get_random_account()
    
    while account_a == account_b:
      account_b = get_random_account()
    
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    # Ask a user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]  
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    
    ## Clear the screen between rounds.
    clear()
    print(logo)
    
    # Give user feedback on their guess.
    # Score keeping.
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      continue_game = False
      print(f"Sorry, that's worng. Final score: {score}.")

game()