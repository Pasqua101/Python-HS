# course: ICS3U1-01
# exercise: ICS3U1-01 option 2 of the final exam
# date: 2020-1-23
# student number: 349612614
# name: Marco Pasqua
# description: This is option 2 of the final exam for ICS3U1-01 the purpose of this program is to take the marks of a class and print them on a vertical histogram with the mean of the marks included
#
#   ______  ___                               ________
# ___   |/  /_____ ___________________      ___  __ \_____ _____________ ____  _______ _
# __  /|_/ /_  __ `/_  ___/  ___/  __ \     __  /_/ /  __ `/_  ___/  __ `/  / / /  __ `/
# _  /  / / / /_/ /_  /   / /__ / /_/ /     _  ____// /_/ /_(__  )/ /_/ // /_/ // /_/ /
# /_/  /_/  \__,_/ /_/    \___/ \____/      /_/     \__,_/ /____/ \__, / \__,_/ \__,_/
#

# For this code I was going to get all of the user input within the function then have it calculate the mean and display all of the grades on the graph. However, when it came to placing it on the graph I decided that I would use conditionals to take all of the numbers in the list and place them in variables that would then place the number of grades that fell in certain categories on the graph.

def student_marks():
    """student_marks() - Takes in the classes marks in a loop and prints them out in a horizontal histogram with the mean of the marks included"""
    # Making a list for the classes marks
    class_marks = []
    # Making a quit variable
    quit = 0

    while quit != 1:
        students_marks = float(input("Please enter your classes marks:"))
        class_marks.append(students_marks)
        print("Here are the current marks for the students in your class", class_marks)
        quit = int(input("Do you wish to see your students marks placed on the histogram and see the class mean? \n(If yes please input -1 otherwise input any other number)."))

        if quit == -1:
            # Finding mean of the marks
            # Finding the number of marks inserted for the mean
            num_marks = len(class_marks)
            # Finding the total of the marks
            total_marks = sum(class_marks)
            mean = total_marks/num_marks
            print("The mean of your classes marks is", round(mean, 2))
            # Sorting the class marks from lowest to highest
            """class_marks.sort
            if 0 <= class_marks[:] <= 49:
                lowest_marks =="""

            # Placing a break statement so the program can stop once the graph has been plotted and the mean has been found
            break

        else:
            # Placing a continue statement here so if the user wants to continue added in marks it will bring the user back to the start of the loop
            continue
student_marks()