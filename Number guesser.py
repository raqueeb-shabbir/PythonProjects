#Import of random module 
import random

#initialising number of tries for user 
tries = 3


#variable for a random integer between 1 and 10
cpu_num = random.randint(1,10)

#Initial intro the game
print("Welcome to the game")
input()
print("You have 3 tries to guess my number from a range of 1 to 10")

#Variable for user's guess
user_guess = int(input())
#Variable for attempt starting at 1 as the while loop will go from 0
attempt = 1

#While loop where attempts of the user must be less than or equal to tries
while attempt <= tries:
    #printing number of attempts made
    print("you have had: " +str(attempt)+ " attempts")
    #if statement to check whether user guess is equal to cpu number, then breaks the while loop
    if int(user_guess) == int(cpu_num):
        print("You win")
        break
    #else statement to replay the game and increment attempt 
    else:
          #where attempt is equal to tries the game is over and you have lost
        if attempt == tries:
            print("You Lose!")
            break
        print("Try again")
        user_guess = input()
    attempt = attempt +1
  





