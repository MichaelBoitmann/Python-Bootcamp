from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


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


# Function to set difficulty
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
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
      play_again = print("Type 'y' if you want to play again and 'n' if not. ")
      if play_again == 'y':
        game()
      else:
        return
    elif guess != answer:
      print("Guess again. ")


game()















# from secrets import randbelow

# print("Welcom to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")

# computer_number = randbelow(101)
# print(f"Pssst, the correct answer is {computer_number}")

# difficulty = input("Choose difficulty. Type 'easy' or 'hard': ")

# if difficulty == 'hard':
#   print("You have 5 attempts remaining to guess the number.")
# else:
#   print("You have 10 attempts remaining to guess the number.")

# player_input = int(input("Make a guess: "))

# keep_guessing = False

# while keep_guessing:
#   if player_input > computer_number:
#     print("")
