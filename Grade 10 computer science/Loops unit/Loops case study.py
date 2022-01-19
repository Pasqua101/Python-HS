"""import random
num1 = random.randint(1,100)

count = 0 
total = 0.0

print num1 
while True:
    count += 1
    guess = input("Guess a number between 1 -100:")
    if guess == num1:
        total = total + 1
        print "Yes, the number is",num1
        g = raw_input("Would you like to play again?")
        if g == 'Yes':
            continue
        else:
            break
    elif guess > num1:
        total = total - 1
        print "Your guess is too high, the number was",num1
        g = raw_input("Would you like to play again?")
        if g == "Yes":
            continue
        else:
            break
    elif guess < num1:
        total = total - 1
        print "Your guess is too low, the number was",num1
        g = raw_input("Would you like to play again?")
        if g == "Yes":
            continue
        else:
            break
print "Out of your",count,"guesses, your average was",round(total/count)"""

#Mr.Cugalari's answer 
import random

num = random.randint(0,100)
count = 0
total = 0.0
while True:
    guess = input("Please enter a number between 1 - 100: ")
    if guess >= 0 and guess <= 100:
        count +=1
        total += guess
        if guess < num:
            print "Your guess is too low"
        elif guess > num:
            print "Your guess is too high"
        elif guess == num:
            print "You are correct"
            break
    else:
        print "Please enter a number between 0-100"
    
print "It took you", count, "guesses"
print "The average of your guesses are", round(total/count, 2)
        

    