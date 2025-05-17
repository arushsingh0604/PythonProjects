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
print("WELCOME TO THE ROCK,PAPER AND SCISSORS GAME")

move1 = int(input("0 for rock,1 for paper and 2 for scissors:"))
if move1 == 0:
    print(f"You chose:\n{rock}")
elif move1 == 1:
    print(f"You chose:\n{paper}")
elif move1 == 2:
    print(f"You chose:\n{scissors}")

move2 = random.randint(0,2)
if move1 > 2 or move1 < 0:
    move2 = 3
    print("you've entered an invalid number")
elif move2 == 0:
    print(f"Computer chose:\n{rock}")
elif move2 == 1:
    print(f"Computer chose:\n{paper}")
elif move2 == 2:
    print(f"Computer chose:\n{scissors}")




if move1 == move2:
    print("DRAW")
elif move1 == 0 and move2 == 1:
    print("YOU LOSE")
elif move1 == 0 and move2 == 2:
    print("YOU WIN!!!")
elif move1 == 1 and move2 == 0:
    print("YOU WIN!!!")
elif move1 == 1 and move2 == 2:
    print("YOU LOSE")
elif move1 == 2 and move2 == 0:
    print("YOU LOSE")
elif move1 == 2 and move2 == 1:
    print("YOU WIN!!!")
