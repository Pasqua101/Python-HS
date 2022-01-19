"""import random

num = random.randint(1,3)

count = 0 
total = 0.0

while True:

    count +=1
    user = input("please enter 1 for rock, 2 for paper, 3 for scissors, <type end to stop>: ")
    if num == 1:
        if user == 1:
            print "tie"
        elif user == 2:
            print "you win!"
        else:
            print "you lose!"
    elif num == 2:
        if user == 1:
            print "you lose!"
        elif user == 2:
            print "tie"
        else:
            print "you lose!"
    else:
        if user == 1:
            print "you win!"
        elif user == 2:
            print "you lose!"
        else:          
            print "tie" 

    if user == "end":
        print "out of the amount of games",count,"you've played, you've won",total
        break"""
    
#Mr.Cuglari's answer    
import random

win = 0
count = 0
while True:
    num = random.randint(1,3)
    user = input("please enter 1 for rock, 2 for paper, 3 for scissors ")
    if user == 1 or user == 2 or user ==3:
        if num == 1:
            if user == 1:
                print "tie"
            elif user == 2:
                print "you win!"
                win +=1
            else:
                print "you lose!"
        elif num == 2:
            if user == 1:
                print "you lose!"
            elif user == 2:
                print "tie"
            else:
                print "you win!"
                win +=1
        else:
            if user == 1:
                print "you win!"
                win +=1
            elif user == 2:
                print "you lose!"
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

print "congratulation your winning percentage is", (float(win)/count)*100,"%"
