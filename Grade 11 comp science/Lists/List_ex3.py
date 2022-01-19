"""
#Creating a list to store the user's marks 
marks = []
count = 0
user_marks = 0 
#Marks will be entered in a while loop and end once the count variable reaches 10
while count != 10:
    user_marks = input("Please enter a mark: ")
    marks.append(user_marks)
    count +=1
    
print(marks)"""

"""#Extension A
#Placing a comma inside the bracket and putting the variable in a loop to print it forward
for x in marks:
    print(x,)

#Extension B
marks.reverse()
print (marks)"""

#Extension C
#Getting total percentage of marks by using the sum function and dividing the variable by the amount of classes
"""total_marks = sum(marks)
print("This is your average",total_marks/10)"""

#Extension D
amt = int(input("How many courses are you entering?"))
grades = []
classes = []

for i in range(amt):
    
    usergrade = float(input("Please enter a mark:"))
    usercourse = input("Please enter your course name:")
    
    grades.append(usergrade)
    classes.append(usercourse)
    
for i in range(len(grades)):
    print(classes[i] + ":", grades[i])
    
totalscore = sum(grades)/len(grades)

print("Your average is,", totalscore)

