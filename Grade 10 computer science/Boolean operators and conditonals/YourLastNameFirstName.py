#Asking for age
age = input("What is your age? ")

if age <= 2: 
    print "Everything is free"

# Asking about Science center and Imax
#Would've of tried to make where if center = Yes it wouldn't print out IMAX question, but it would've been complicated for the student part
center = raw_input("Are you only attending the science center? ")

IMAX = raw_input("Are you only watching an IMAX film?")

if age >= 3 and age <= 12:
    if IMAX == 'Yes':
        IMAX = 9
        print "The total cost is $",IMAX

if age >= 3 and age <= 12:
    if center == 'Yes':
        center = 13
        print "The total cost is $",center

if age >= 3 and age <= 12:
    if center == 'No':
        center = 13
    if IMAX == 'No':
        IMAX = 9
        print "The total cost is $",center+IMAX-3

if age >= 18 and age <=64:
    if center == 'No':
        center = 22
        if IMAX == "No":
            IMAX = 13
            print"The total cost is $",center+IMAX-7

if age >= 18 and age <=64:
    if center == 'Yes':
        center = 22
        print"The total cost is $",center

if age >= 18 and age <=64:
    if IMAX == "Yes":
        IMAX = 13
        print"The total cost is $",IMAX
        
if age >= 65:
    if IMAX == 'Yes':
        IMAX = 9
        print "The total cost is $",IMAX

if age >= 65:
    if center == 'Yes':
        center = 16
        print "The total cost is $",center

if age >= 65:
    if center == 'No':
        center = 16
    if IMAX == 'No':
        IMAX = 9
        print "The total cost is $",center+IMAX-3
#Made this a else statement so adults, infants and senior don't need to answer it
else: 
    student = raw_input("Are you a student? ")
#Using if, and statements for age
#Then if center == Yes the center would change to it's price and get rid of IMAX. Plus the same would be for IMAX
#Using nested if statements so center or Imax will change. Plus it will work if the user puts in Yes or No for student

if age >= 13 and age <=17:
        if center == 'Yes':
            center = 16
            print "The total cost is $",center

if age >= 13 and age <=17:
    if student == 'Yes':
        if center == 'No':
            center = 16
            if IMAX == "No":
                IMAX = 9
                print"The total cost is $",center+IMAX-3

if age >= 13 and age <=17:
    if student == 'No':
        if center == 'No':
            center = 16
            if IMAX == "No":
                IMAX = 9
                print"The total cost is $",center+IMAX

if age >= 13 and age <=17:
    if IMAX == "Yes":
        IMAX = 9
        print"The total cost is $",IMAX
