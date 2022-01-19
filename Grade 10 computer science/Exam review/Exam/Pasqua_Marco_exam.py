#Making a while loop so a infinite amount of marks can be placed
#Making a list to store marks between 0 - 49, 50 - 59, 60 - 69, etc

#List for marks from 0 -49
lowest_marks = []
#List for marks from 50 - 59
fifthy_marks = []
#List for marks from 60 - 69
sixities_marks = []
#List for marks from 70 - 79
seventies_marks = []
#list for marks from 80 - 100
highest_marks = []
#List for all the marks that are entered
total_marks = []

#Making a count statement so I can find average
count = 0

while True:
    #Asking the user to put in marks 
    marks = input("Please enter a mark for one of your students <type -1 to stop entering marks>: ")
    
    #Marks from 0 - 49
    if marks >= 0 and marks <= 49:
        #Using .append to add marks into a list
        lowest_marks.append(marks)
        #Count statement used to determine how many marks are entered
        count +=1
        #Using a .append statement for total marks so I can find the average
        total_marks.append(marks)
    
    #Marks from 50 - 59    
    elif marks >= 50 and marks <= 59:
        #Using .append to add marks into a list
        fifthy_marks.append(marks)
        #Count statement used to determine how many marks are entered
        count +=1
        #Using a .append statement for total marks so I can find the average
        total_marks.append(marks)
    
    #Marks from 60 - 69
    elif marks >= 60 and marks <= 69:
        #Using .append to add marks into a list
        sixities_marks.append(marks)
        #Count statement used to determine how many marks are entered
        count +=1
        #Using a .append statement for total marks so I can find the average
        total_marks.append(marks)
    
    #Marks from 70 - 79
    elif marks >= 70 and marks <= 79:
        #Using .append to add marks into a list
        seventies_marks.append(marks)
        #Count statement used to determine how many marks are entered
        count +=1
        #Using a .append statement for total marks so I can find the average
        total_marks.append(marks)
    
    #Marks from 80 - 89
    elif marks >= 80 and marks <= 100:
        #Using .append to add marks into a list
        highest_marks.append(marks)
        #Count statement used to determine how many marks are entered
        count +=1
        #Using a .append statement for total marks so I can find the average
        total_marks.append(marks)
   #Breaking the loop
    elif marks == -1:
        #breaking the list when -1 is entered
        break
    #Showing user what marks they entered
    print "Marks entered",total_marks

#Making a total for all of the list so I can find average
total = sum(lowest_marks) + sum(fifthy_marks) + sum(sixities_marks) + sum(seventies_marks) + sum(highest_marks)

#Finding average
average = total/count

#Printing marks for the students in the class
print "0-49:",lowest_marks
print "50-59:",fifthy_marks
print "60-69:",sixities_marks
print "70-79:",seventies_marks
print '80-100:',highest_marks
#Printing average
print "Average (Mean)",average,"%"
