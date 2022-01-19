from random import randint

while True:
    guess = float(input("Guess your magic number from 1 -100:"))
    number =  randint(1,100)
    if guess == number:
        print ("Yay! You guess the right number")
        break
    elif guess != number:
        print ("Sorry, but the correct number was",number,"Try again")