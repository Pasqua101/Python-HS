#Question 1
 
"""a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for b in a:
    if b % 2 == 0:
        print "This is the even numbers in the list"
        print b"""

#Question 2
"""import random

win = 0
count = 0
while True:
    num = input("Player 1, please enter 1 for rock, 2 for paper, 3 for scissors ")
    user = input("Player 2,please enter 1 for rock, 2 for paper, 3 for scissors ")
    if user == 1 or user == 2 or user ==3:
        if num == 1:
            if user == 1:
                print "tie"
            elif user == 2:
                print "Player 2 wins!"
                win2 +=1
            else:
                print "Player 1 wins!"
                win1 +=1
        elif num == 2:
            if user == 1:
                print "Player 1 wins!"
                win1 +=1
            elif user == 2:
                print "tie"
            else:
                print "Player 2 wins!"
                win2 +=1
        else:
            if user == 1:
                print "Player 2 wins!"
                win2 +=1
            elif user == 2:
                print "Player 1 wins!"
                win1 +=1
            else:          
                print "tie"
        
        count +=1
    else:
        print "invalid input"
        #We will get an error if they enter letters. 
        #We can switch user = input() to raw_input and caste everything to int to avoid this
        
    game = raw_input("Do you want to play again? Yes or no")
    if game == "yes" or game == "Yes":
        print "Here we go"
    else:
        break

print "congratulations Player 1's winning percentage is", (float(win1)/count)*100,"%"
print "congratulations Player 2's winning percentage is", (float(win2)/count)*100,"%"""

#Question 3

"""import random

num = random.randint(1,9)
count = 0
total = 0.0
while True:
    guess = raw_input("Please enter a number between 1 - 9<type exit to stop>: ")
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
        elif guess == "exit":
            break
    else:
        print "Please enter a number between 0-100"
    
print "It took you", count, "guesses"
print "The average of your guesses are", round(total/count, 2)"""
