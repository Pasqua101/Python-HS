import random

num = random.randint(1,3)

user = input("please enter 1 for rock, 2 for paper, 3 for scissors ")

if num == 1 and user == 1:
    print "tie"
elif num == 1 and user == 2:
    print "you win!"
elif num == 1 and user == 3:
    print "you lose!"
elif num == 2 and user == 1:
    print "you lose!"
elif num == 2 and user == 2:
    print "tie"
elif num == 2 and user == 3:
    print "you lose!"
elif num == 3 and user == 1:
    print "you win!"
elif num == 3 and user == 2:
    print "you lose!"
else:          #Last option used else instead of elif num == 3 and user == 3:
    print "tie"

 

#Advanced selections

import random

num = random.randint(1,3)

user = input("please enter 1 for rock, 2 for paper, 3 for scissors ")

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