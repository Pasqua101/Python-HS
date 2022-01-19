#Question 1

"""count = 0
total = 0.0 

while True: 
    count +=4
    mark1 = input('Please enter the mark for your first class')
    mark2 = input("Please enter the mark for your second class")
    mark3 = input("Please enter the mark for your third class")
    mark4 = input("Please enter the mark for your fourth class")
    break 

if mark1 >= 50:
    print "You passed your first course"
    total = total + 1
elif mark1 <= 49:
    print "You failed your first course"
if mark2 >= 50:
    print "You passed your second course"
    total = total + 1
elif mark2 <= 49:
    print "You failed your second course"
if mark3 >= 50:
    print "You passed your third course"
    total = total + 1
elif mark3 <= 49:
    print "You failed your third course"
if mark4 >= 50:
    print "You passed your fourth course"
    total = total + 1
elif mark4 <=49:
    print "You failed your fourth course"
        
print "Out of your",count,"courses, you passed",total,"courses"""

#Question 2

"""grain = 1 

for tile in range(64):
    print grain,"grains"
    if tile == 64:
        break
    grain = grain*2
print "\n"
print "Therefore, the king owes the inventor",grain/7000,"pounds of grains."""
#Question 3 

macDonaldVote = 0.0
mackenzieVote = 0.0
abbottVote = 0.0


print "Type 1 for Sir John A Macdonald, 2 for Alexander Mackenzie and 3 for Sir John Abbot. Make sure you know who you'r voting for <Type 0 to exit>"

while True: 

    vote = input("enter your vote<type 0 to stop>") 
    
    if vote == 1:
        macDonaldVote += 1
    elif vote == 2: 
        mackenzieVote += 1
    elif vote == 3:
        abbottVote += 1
    elif vote == 0:
        break
if macDonaldVote > mackenzieVote and macDonaldVote > abbottVote:
    print "Sir John A Macdonald won"
elif mackenzieVote> macDonaldVote and mackenzieVote > abbottVote:
    print ("Alexander Mackenzie won")
elif abbottVote > macDonaldVote and abbottVote > mackenzieVote:
    print "John Abbott won"
else: 
    print "Tie"
    
totalVotes = mackenzieVote+macDonaldVote+abbottVote

print "Sir John A MacDonald earned",(float(macDonaldVote/totalVotes)*100),"%"
print "Alexander Mackenzie earned",(float(mackenzieVote/totalVotes)*100),"%"
print "John Abbot earned",(float(abbottVote/totalVotes)*100),"%"
    
#Question 4 
"""while True:
    
    string=raw_input("Enter palindrome such as ana, please enter your string in lower case:")
    if(string==string[::-1]):
        print("The string is a palindrome")
    else:
        print("The string isn't a palindrome")"""
    
#Question 5
"""while True:
    user = raw_input("Please enter your user name:")
    password = input("Welcome, please enter your password:")
    if password ==123:
        print "Welcome",user,"to the S.H.E.I.L.D."
        break
    else:
        print "There was an error with your username or password. Please try again."""