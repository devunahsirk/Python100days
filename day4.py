print("Welcome to the Rock, Paper, Scissors Game!")
# User input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissor\n"))
print("You choose")
if user_choice==0:
  print('''
           _______
       ---'   ____)
             (_____)
             (_____)
             (____)
       ---.__(___)
       ''')
elif user_choice==1:
  print('''
           _______
       ---'   ____)____
                 ______)
                 _______)
                _______)
       ---.__________)
       ''')
else:
  print('''
           _______
       ---'   ____)____
                 ______)
              __________)
             (____)
       ---.__(___)
       ''')

#computer choice
import random

print("Computer choose")
computer=random.randint(0,2)
if computer==0:
  print('''
           _______
       ---'   ____)
             (_____)
             (_____)
             (____)
       ---.__(___)
       ''')
elif computer==1:
  print('''
           _______
       ---'   ____)____
                 ______)
                 _______)
                _______)
       ---.__________)
       ''')
else:
  print('''
           _______
       ---'   ____)____
                 ______)
              __________)
             (____)
       ---.__(___)
       ''')


if user_choice==0:
  if computer==0:
    print("Its a tie")
  elif computer==1:
    print("Computer wins")
  else:
    print("You win")

elif user_choice==1:
  if computer==1:
    print("Its a tie")
  elif computer==0:
    print("You win")
  else:
    print("Computer wins")

else:
  if computer==0:
    print("Computer wins")
  elif computer==1:
    print("You win")
  else:
    print("Its a tie")
