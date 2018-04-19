


import random


print("Guess a number from 1 to 100: ")


def guess():

    num=random.randint(1,100)

    userNumber= 


while userNumber >0 :
    guess = int(input("Is it..."))
    if guess==num:
        print("Hoorey! You guessed it right!")
    elif guess < num:
        print("It's bigger")
    elif guess>num:
        print("It's not so big.")

