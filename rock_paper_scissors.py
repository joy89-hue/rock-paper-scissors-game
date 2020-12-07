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
player = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors: "))

if player == 0:
  print(f"Player choose: {rock}")
elif player == 1:
  print(f"Player choose: {paper}")
else:
  print(f"Player choose: {scissors}")

num = [0, 1, 2]
generated_choice = choice(num)
computer = generated_choice

if generated_choice == 0:
  print(f"Computer choose: {rock}")

elif generated_choice == 1:
  print(f"Computer choose: {paper}")
else:
  print(f"Computer choose: {scissors}")  

if player == computer:
  print("Its a tie")
elif player> computer:
  print("You win!!")
else:
  print("You loose:(")
