limit = 60 

speed = input("How fast are you driving? ")

if speed > limit and speed <= 80:
    print "You are speeding and your fine is $100"
elif speed >= 81 and speed <= 90:
    print "You are speeding and your fine is $270"
elif speed > 91:
    print "You are speeding and your fine is $500"
elif speed <= limit:
    print "Congratulations, you are within the speed limit!"