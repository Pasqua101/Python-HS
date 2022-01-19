import random

num1 = random.randint(1,10)

count = 0 
total = 0.0

for num2 in range(5):
    count +=1
    num2 = input("Guess a number that I am thinking from 1 - 10 (You have 5 guess), <type end to stop>")
    if num2 == num1:
        print 'You are a psychic!'
        total += num2 #total = total + num2
        break
    total += num2
    if num2 == "end":
        break    
    if num2!=num1:
        if count == 5: 
            print "Looks like you ran out of guesses"
            break
    print "Try again"

print "out of your",count,"guesses the average number of guess is",total