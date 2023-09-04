import random
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

game_images = [rock ,paper, scissors]
user_choice = int(input("What do you choose, Type 0 for Rock, 1 for scissors, 2 for paper.\n"))
print(game_images[user_choice])
computer_choice= random.randint(0,2)
print("computer chose:")
print(game_images[computer_choice])
print(f"Computer chose{computer_choice}")
if user_choice == 0 and computer_choice == 2:
  print("You win")
elif user_choice >=3:
  print("You typed an invalid number, you lose:)")
elif computer_choice>user_choice:
  print("You lose")
elif user_choice>computer_choice:
  print("You win")
elif computer_choice==user_choice:
  print("It is a draw")

