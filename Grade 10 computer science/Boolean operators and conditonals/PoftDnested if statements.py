"""grade = input('Please enter your grade: ')
gender = raw_input("Please enter the first letter of your gender: ")

if grade == 9 or grade == 10:
    if gender == 'M':
        print "You are on the junior boys team"
    elif gender == 'F':
        print "You are on the junior girls team"
if grade == 11 or grade == 12: 
    if gender == 'M':
        print "You are on the senior boys team"
    elif gender == 'F':
        print "You are on the senior girls team"""
#Cugliari's answer
grade = input("Please enter grade ")
gender = raw_input("Please enter gender m for male, f for female ")

if grade == 9 or grade == 10:
    if gender == "m":
        print "you are on the Junior boys team"
    elif gender == "f":
        print "you are on the Junior girls team"
    else:
        print "Invalid input"
        
elif grade == 11 or grade == 12:
    if gender == "m":
        print "you are on the Senior boys team"
    elif gender == "f":
        print "you are on the Senior girls team"
    else:
        print "Invalid input"
        
else:
    print "wrong grade entered"