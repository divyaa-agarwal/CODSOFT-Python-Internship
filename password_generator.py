#IMPORTING THE REQUIRED MODULES
import random
import string

#TAKING THE LENGTH OF THE PASSWORD AS INPUT
n=int(input("Enter the length of the password: "))

#GENERATING THE PASSWORD USING THE CHOICE FUNCTION FROM THE RANDOM MODULE
characters=string.ascii_letters + string.digits + string.punctuation

#INITIALIZING AN EMPTY STRING TO STORE THE GENERATED PASSWORD
password=""

#LOOPING THROUGH THE RANGE OF THE LENGTH OF THE PASSWORD AND ADDING A RANDOM CHARACTER TO THE PASSWORD STRING IN EACH ITERATION
for i in range(n):
    password+=random.choice(characters)

#PRINTING THE GENERATED PASSWORD
print("Generated password: ", password)
