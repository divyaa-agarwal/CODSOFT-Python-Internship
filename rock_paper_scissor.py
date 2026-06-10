# This is a simple implementation of the Rock-Paper-Scissors game in Python.
import random

print("-"*5,"Welcome to Rock-Paper-Scissors Game!","-"*5)
print("Rules: \nRock beats Scissors \nScissors beats Paper \nPaper beats Rock")
print("-"*50)
print("Let's start the game!")
print("-"*50)
print("Type quit to exit the game.")

while True:   
#TAKING THE USER'S CHOICE AS INPUT
 user_choice=input("Enter your choice (rock, paper, scissors): ").strip().lower()
 
 if user_choice=="quit":
    print("Thanks for playing! Goodbye!")
    break
#VALIDATING THE USER'S CHOICE
 if user_choice not in ["rock", "paper", "scissors"]:
    print("Invalid input! Please enter rock, paper, or scissors.")
    continue

#GENERATING THE COMPUTER'S CHOICE USING THE CHOICE FUNCTION FROM THE RANDOM MODULE
 choices=["rock", "paper", "scissors"]

 computer_choice=random.choice(choices)

#PRINTING THE COMPUTER'S CHOICE
 print("Computer's choice: ", computer_choice)

#DETERMINING THE WINNER BASED ON THE USER'S CHOICE AND THE COMPUTER'S CHOICE

 if user_choice==computer_choice:
    print("It's a tie!")

 elif user_choice=="rock":#IF THE USER CHOOSES ROCK, THEN CHECK THE COMPUTER'S CHOICE
    if computer_choice=="scissors":
        print("You win!")
    else:
        print("Computer wins!")

 elif user_choice=="paper":#IF THE USER CHOOSES PAPER, THEN CHECK THE COMPUTER'S CHOICE
     if computer_choice=="rock":
        print("You win!")
     else:
        print("Computer wins!")

 else: #IF THE USER CHOOSES SCISSORS, THEN CHECK THE COMPUTER'S CHOICE
     if computer_choice=="paper":
        print("You win!")
     else:
        print("Computer wins!")        
