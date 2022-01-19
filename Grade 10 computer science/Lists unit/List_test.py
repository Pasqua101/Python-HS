#making empty lists and importing random function

import random 

marks = []
random_mark = []
empty =[]

#putting in values and input statements for marks

mark1 = 0
mark2 = 0
mark3 = 0

mark1 = input("Please enter your first mark: ")
mark2 = input("Please enter your second mark: ")
mark3 = input("Please enter your third mark: ")
#making a total mark for average
total_mark = mark1 + mark2 + mark3
#Adding inputs from mark1, 2 and 3 to the marks list
marks.append(mark1)
marks.append(mark2)
marks.append(mark3) 

#Now making random marks and making new variables
random_mark1 = 0
random_mark2 = 0
random_mark3 = 0

random_mark1 = random.randint(1,100)
random_mark2= random.randint(1,100)
random_mark3 = random.randint(1,100)
#making a total for average
randomtotal = random_mark1 + random_mark2 + random_mark3 

#adding randomly generated numbers into list
random_mark.append(random_mark1)
random_mark.append(random_mark2)
random_mark.append(random_mark3)

#storing numbers in for loops and printing them forwards and backwards
for x in range(1):
    empty.append(random_mark)
for x in range(1):
    empty.append(marks)
    
print empty

for x in reversed(empty):
    print x
    
# finding average 

if total_mark < randomtotal:
    average = (float(total_mark/randomtotal)*100)

if randomtotal < total_mark:
    average = (float(randomtotal/total_mark)*100)

print "The average mark is:",average

#Telling person if they are or aren't failing the average 
if total_mark < randomtotal:
    print "You have a failing average"
elif total_mark > randomtotal:
    print "You have passed the average"
else:
    print "You have the same average"
    
