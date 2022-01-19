import time
import random
import threading
name = raw_input("Hello, what is your name?")
name2 = raw_input("What is your partner's name?")
time.sleep(1)
print "Hello,", name, "and", name2
time.sleep(1)
print "Welcome to the Bomb Squad!"
time.sleep(2)
print "There is a bomb that is needed to be defused in your area!"
time.sleep(3)
print "Here is your time zone:", time.tzname
time.sleep(3)
print "Hint: When inputting which wire to cut, type it in the format 'COLOUR OF THE WIRE-#'"
time.sleep(4)
print "You are being transported to the bomb defusal site in:"
time.sleep(1)
print "3"
time.sleep(1)
print "2"
time.sleep(1)
print "1"
time.sleep(1)
def gameover():
    print "\nBOOM!!! \nYOU HAVE DIED BECAUSE YOU RAN OUT OF TIME."
    exit()

def game():
    wireCount = random.randint(3,6)
    
    if wireCount == 3:
        print "=====================WIRES====================="
        wire1 = random.randint(1,5)
        wire2 = random.randint(1,5)
        wire3 = random.randint(1,5)
                
        #wire1 colours
        if wire1 == 1:
            wire1 = "RED-1"
        elif wire1 == 2:
            wire1 = "BLUE-1"
        elif wire1 == 3:
            wire1 = "WHITE-1"
        elif wire1 == 4:
            wire1 = "BLACK-1"
        elif wire1 == 5:
            wire1 = "YELLOW-1"
    
        #wire2 colours
        if wire2 == 1:
            wire2 = "RED-2"
        elif wire2 == 2:
            wire2 = "BLUE-2"
        elif wire2 == 3:
            wire2 = "WHITE-2"
        elif wire2 == 4:
            wire2 = "BLACK-2"
        elif wire2 == 5:
            wire2 = "YELLOW-2"
    
        #wire3 colours
        if wire3 == 1:
            wire3 = "RED-3"
        elif wire3 == 2:
            wire3 = "BLUE-3"
        elif wire3 == 3:
            wire3 = "WHITE-3"
        elif wire3 == 4:
            wire3 = "BLACK-3"
        elif wire3 == 5:
            wire3 = "YELLOW-3"
            
        wireTotal = wire1 + wire2 + wire3
           
        print wire1
        print wire2
        print wire3
        
        print "You have 30 seconds to diffuse the bomb with your partner. Use the manual provided to you."
        
        timer = threading.Timer(30.0,gameover)
        timer.start()
        cutColor = raw_input("Cut:")
    
            
        if (wireTotal.count("RED") == 0) and (cutColor == wire2):
            print "CONGRATULATIONS! THE BOMB HAS BEEN DEFUSED!"
        elif (wire3 == "WHITE-3") and (cutColor == wire3):
            print "CONGRATULATIONS! THE BOMB HAS BEEN DEFUSED!"
        elif (wireTotal.count("BLUE") > 1) and (cutColor.count("BLUE" == 1)):
            print "CONGRATULATIONS! THE BOMB HAS BEEN DEFUSED!"
        elif (cutColor == wire3):
            print "CONGRATULATIONS! THE BOMB HAS BEEN DEFUSED!"
        else:
            print "BOOM!!! \nYOU HAVE DIED FROM FAILING BY CUTTING THE WRONG WIRE."
            exit()
    
    elif wireCount == 4:
        print "=====================WIRES====================="
        wire1 = random.randint(1,5)
        wire2 = random.randint(1,5)
        wire3 = random.randint(1,5)
        wire4 = random.randint(1,5)
        
        #wire1 colours
        if wire1 == 1:
            wire1 = "RED-1"
        elif wire1 == 2:
            wire1 = "BLUE-1"
        elif wire1 == 3:
            wire1 = "WHITE-1"
        elif wire1 == 4:
            wire1 = "BLACK-1"
        elif wire1 == 5:
            wire1 = "YELLOW-1"
    
        #wire2 colours
        if wire2 == 1:
            wire2 = "RED-2"
        elif wire2 == 2:
            wire2 = "BLUE-2"
        elif wire2 == 3:
            wire2 = "WHITE-2"
        elif wire2 == 4:
            wire2 = "BLACK-2"
        elif wire2 == 5:
            wire2 = "YELLOW-2"
    
        #wire3 colours
        if wire3 == 1:
            wire3 = "RED-3"
        elif wire3 == 2:
            wire3 = "BLUE-3"
        elif wire3 == 3:
            wire3 = "WHITE-3"
        elif wire3 == 4:
            wire3 = "BLACK-3"
        elif wire3 == 5:
            wire3 = "YELLOW-3"
            
        #wire4 colours
        if wire4 == 1:
            wire4 = "RED-4"
        elif wire4 == 2:
            wire4 = "BLUE-4"
        elif wire4 == 3:
            wire4 = "WHITE-4"
        elif wire4 == 4:
            wire4 = "BLACK-4"
        elif wire4 == 5:
            wire4 = "YELLOW-4"
            
        wireTotal = wire1 + wire2 + wire3 + wire4
           
        print wire1
        print wire2
        print wire3
        print wire4
        
        print "You have 30 seconds to diffuse the bomb with your partner. Use the manual provided to you."
        
        timer = threading.Timer(30.0,gameover)
        timer.start()    
        cutColor = raw_input("Cut:")
        
        if (wireTotal.count("RED") > 1) and (cutColor.count("RED") == 1):
            print "CONGRATULATIONS! THE BOMB HAS BEEN DEFUSED!"
        elif (wire4 == "YELLOW-4") and (wireTotal.count("RED") == 0) and (cutColor == wire1):
            print "CONGRATULATIONS! THE BOMB HAS BEEN DEFUSED!"
        elif (wireTotal.count("BLUE")) and (cutColor == wire1):
            print "CONGRATULATIONS! THE BOMB HAS BEEN DEFUSED!"
        elif (wireTotal.count("YELLOW") > 1) and (cutColor == wire2):
            print "CONGRATULATIONS! THE BOMB HAS BEEN DEFUSED!"
        elif (cutColor == wire2):
            print "CONGRATULATIONS! THE BOMB HAS BEEN DEFUSED!"
        else:
            print "BOOM!!! \nYOU HAVE DIED FROM FAILING BY CUTTING THE WRONG WIRE."
            exit()
    
    elif wireCount == 5:
        print "=====================WIRES====================="
        wire1 = random.randint(1,5)
        wire2 = random.randint(1,5)
        wire3 = random.randint(1,5)
        wire4 = random.randint(1,5)
        wire5 = random.randint(1,5)
        
        #wire1 colours
        if wire1 == 1:
            wire1 = "RED-1"
        elif wire1 == 2:
            wire1 = "BLUE-1"
        elif wire1 == 3:
            wire1 = "WHITE-1"
        elif wire1 == 4:
            wire1 = "BLACK-1"
        elif wire1 == 5:
            wire1 = "YELLOW-1"
    
        #wire2 colours
        if wire2 == 1:
            wire2 = "RED-2"
        elif wire2 == 2:
            wire2 = "BLUE-2"
        elif wire2 == 3:
            wire2 = "WHITE-2"
        elif wire2 == 4:
            wire2 = "BLACK-2"
        elif wire2 == 5:
            wire2 = "YELLOW-2"
    
        #wire3 colours
        if wire3 == 1:
            wire3 = "RED-3"
        elif wire3 == 2:
            wire3 = "BLUE-3"
        elif wire3 == 3:
            wire3 = "WHITE-3"
        elif wire3 == 4:
            wire3 = "BLACK-3"
        elif wire3 == 5:
            wire3 = "YELLOW-3"
            
        if wire4 == 1:
            wire4 = "RED-4"
        elif wire4 == 2:
            wire4 = "BLUE-4"
        elif wire4 == 3:
            wire4 = "WHITE-4"
        elif wire4 == 4:
            wire4 = "BLACK-4"
        elif wire4 == 5:
            wire4 = "YELLOW-4"
    
        if wire5 == 1:
            wire5 = "RED-5"
        elif wire5 == 2:
            wire5 = "BLUE-5"
        elif wire5 == 3:
            wire5 = "WHITE-5"
        elif wire5 == 4:
            wire5 = "BLACK-5"
        elif wire5 == 5:
            wire5 = "YELLOW-5"
    
        wireTotal = wire1 + wire2 + wire3 + wire4 + wire5
           
        print wire1
        print wire2
        print wire3
        print wire4
        print wire5
        
        print "You have 30 seconds to diffuse the bomb with your partner. Use the manual provided to you."
        
        timer = threading.Timer(30.0,gameover)
        timer.start()
     
        cutColor = raw_input("Cut:")
        
        if (wire5 == "BLACK-5") and cutColor == wire4:
            print "CONGRATULATIONS! THE BOMB HAS BEEN DEFUSED!"
        elif (wireTotal.count("RED") == 1) and (wireTotal.count("YELLOW") > 1) and (cutColor == wire1):
            print "CONGRATULATIONS! THE BOMB HAS BEEN DEFUSED!"
        elif (wireTotal.count("BLACK") == 0) and (cutColor == wire2):
            print "CONGRATULATIONS! THE BOMB HAS BEEN DEFUSED!"
        elif (cutColor == wire1):
            print "CONGRATULATIONS! THE BOMB HAS BEEN DEFUSED!"
        else:
            print "BOOM!!! \nYOU HAVE DIED FROM FAILING BY CUTTING THE WRONG WIRE."
            exit()
            
    elif wireCount == 6:
        print "=====================WIRES====================="
        wire1 = random.randint(1,5)
        wire2 = random.randint(1,5)
        wire3 = random.randint(1,5)
        wire4 = random.randint(1,5)
        wire5 = random.randint(1,5)
        wire6 = random.randint(1,5)
        
        #wire1 colours
        if wire1 == 1:
            wire1 = "RED-1"
        elif wire1 == 2:
            wire1 = "BLUE-1"
        elif wire1 == 3:
            wire1 = "WHITE-1"
        elif wire1 == 4:
            wire1 = "BLACK-1"
        elif wire1 == 5:
            wire1 = "YELLOW-1"
    
        #wire2 colours
        if wire2 == 1:
            wire2 = "RED-2"
        elif wire2 == 2:
            wire2 = "BLUE-2"
        elif wire2 == 3:
            wire2 = "WHITE-2"
        elif wire2 == 4:
            wire2 = "BLACK-2"
        elif wire2 == 5:
            wire2 = "YELLOW-2"
    
        #wire3 colours
        if wire3 == 1:
            wire3 = "RED-3"
        elif wire3 == 2:
            wire3 = "BLUE-3"
        elif wire3 == 3:
            wire3 = "WHITE-3"
        elif wire3 == 4:
            wire3 = "BLACK-3"
        elif wire3 == 5:
            wire3 = "YELLOW-3"
            
        if wire4 == 1:
            wire4 = "RED-4"
        elif wire4 == 2:
            wire4 = "BLUE-4"
        elif wire4 == 3:
            wire4 = "WHITE-4"
        elif wire4 == 4:
            wire4 = "BLACK-4"
        elif wire4 == 5:
            wire4 = "YELLOW-4"
    
        if wire5 == 1:
            wire5 = "RED-5"
        elif wire5 == 2:
            wire5 = "BLUE-5"
        elif wire5 == 3:
            wire5 = "WHITE-5"
        elif wire5 == 4:
            wire5 = "BLACK-5"
        elif wire5 == 5:
            wire5 = "YELLOW-5"
            
        if wire6 == 1:
            wire6 = "RED-6"
        elif wire6 == 2:
            wire6 = "BLUE-6"
        elif wire6 == 3:
            wire6 = "WHITE-6"
        elif wire6 == 4:
            wire6 = "BLACK-6"
        elif wire6 == 5:
            wire6 = "YELLOW-6"
    
        wireTotal = wire1 + wire2 + wire3 + wire4 + wire5 + wire6
           
        print wire1
        print wire2
        print wire3
        print wire4
        print wire5
        print wire6
        
        print "You have 30 seconds to diffuse the bomb with your partner. Use the manual provided to you."
        
        timer = threading.Timer(30.0,gameover)
        timer.start()
        
        cutColor = raw_input("Cut:")
        
        if (wireTotal.count("YELLOW") == 0) and (cutColor == wire3):
            print "CONGRATULATIONS! THE BOMB HAS BEEN DEFUSED!"
        elif (wireTotal.count("YELLOW") == 1) and (wireTotal.count("WHITE") > 1) and (cutColor == wire4):
            print "CONGRATULATIONS! THE BOMB HAS BEEN DEFUSED!"
        elif (wireTotal.count("RED") == 0) and (cutColor == wire6):
            print "CONGRATULATIONS! THE BOMB HAS BEEN DEFUSED!"
        elif (cutColor == wire4):
            print "CONGRATULATIONS! THE BOMB HAS BEEN DEFUSED!"
        else:
            print "BOOM!!! \nYOU HAVE DIED FROM FAILING BY CUTTING THE WRONG WIRE."
            exit()
            
    timer.cancel()
    
game()