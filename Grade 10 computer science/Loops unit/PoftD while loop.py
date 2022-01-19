count = 0
total = 0
while True: 
    num1 = input("Please enter a number from 1 - 20: <end to exit>")
    if num1 == "end":
        break 
    if num1 >= 1 and num1 <= 20:
        print "Thank you for listening"
        break 
    else:
        #print 'Sorry, this number is out of my range'
        count +=1
        total +=1
        if total == 3:
            print "Please stop being annoying"
        elif total == 5:
            print "I'm warning you! Please enter the right number!"
        elif total == 6:
            print "Terminate your program"
            exit ()
