from random import choice


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Game setup
"""
3 SIMPLE RULES FOR RPS:
Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.
"""
game_image = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors: "))

if user_choice in [0, 1, 2]:
  print("You choose:\n")
  print(game_image[user_choice])

  computer_choice = randint(0, 2)
  print("Computer choose:\n")
  print(game_image[computer_choice])

  if user_choice == computer_choice:
    print("Its a tie")
  else:
    if user_choice == 0:
      if computer_choice == 1:
        print("You lose..")
      else:
        print("You win!")

    elif user_choice == 1:
      if computer_choice == 2:
        print("You lose..")
      else:
        print("You win!")
    elif user_choice == 2:
      if computer_choice == 1:
        print("You win!")
      else:
        print("You lose..")  
else:
  print("You typed invalid literal. You lose!")
