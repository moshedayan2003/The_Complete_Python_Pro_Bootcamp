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

# My Answer:
# user_choice = int(input("Type \'0\' for rock, \'1\' for paper, and \'2\' for scissors: "))
# if user_choice == 0:
#     print(rock)
# elif user_choice == 1:
#     print(paper)
# elif user_choice == 2:
#     print(scissors)
# else:
#     print("You typed and invalid number. You lose!")
#
# print("Computer chose:")
# computer_choice = random.randint(0, 2)
# if computer_choice == 0:
#     print(rock)
# elif computer_choice == 1:
#     print(paper)
# else:
#     print(scissors)
#
# if ((user_choice == 0 and computer_choice == 1) or
#     (user_choice == 1 and computer_choice == 2) or
#     (user_choice == 2 and computer_choice == 0)):
#        print("You lose!")
# elif(user_choice == computer_choice):
#     print("Draw")
# else:
#     print("You win!")




# Angela's answer
game_images = [rock, paper, scissors]

user_choice = int(input("Type \'0\' for rock, \'1\' for paper, and \'2\' for scissors: "))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == computer_choice:
    print("Draw")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
