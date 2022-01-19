# course: ICS3U1-01
# exercise: ICS3U1-01 option 3 of the final exam
# date: 2020-1-23
# student number: 349612614
# name: Marco Pasqua
# description: This is option 3 of the final exam for ICS3U1-01 the purpose of this program is to take the user's marks and find the meadian and average of them.
#
#   ______  ___                               ________
# ___   |/  /_____ ___________________      ___  __ \_____ _____________ ____  _______ _
# __  /|_/ /_  __ `/_  ___/  ___/  __ \     __  /_/ /  __ `/_  ___/  __ `/  / / /  __ `/
# _  /  / / / /_/ /_  /   / /__ / /_/ /     _  ____// /_/ /_(__  )/ /_/ // /_/ // /_/ /
# /_/  /_/  \__,_/ /_/    \___/ \____/      /_/     \__,_/ /____/ \__, / \__,_/ \__,_/
#

def markAvgMean():
    """markAveMean() - Takes in a number of marks that the user inputs in the loop and prints the average of the marks and the median."""
    # Making a quit variable if the user is finished they can make it equal -1
    quit = 0
    # List for student's marks
    stud_marks = []
    num_marks = 0
    while quit != -1:

        # Making the user's marks a float so it can keep decimals from the students marks
        user_marks = float(input("Please enter the marks you wish to have:"))
        stud_marks.append(user_marks)
        print("Here are the current marks you wish to have", stud_marks)
        quit = int(input("Do you wish quit and see what your average is? \n(If yes, please enter -1. If no, please enter any number other than -1.)"))

        if quit == -1:
            # Taking in the number of marks that will be used to find average
            num_marks = len(stud_marks)
            # Taking in the sum of the marks for average
            total_marks = sum(stud_marks)
            # Finding average of the marks
            avg_marks = total_marks/num_marks
            # Rounding the marks to 2 decimal places
            print("The average of you marks is ", round(avg_marks,2))

            # Finding median

            # Sorting the list
            stud_marks.sort()
            # Finding position of the median
            if len(stud_marks) % 2 == 0:
                first_median = stud_marks[len(stud_marks) // 2]
                second_median = stud_marks[len(stud_marks) // 2 - 1]
                median = (first_median + second_median) / 2
            else:
                median = stud_marks[len(stud_marks) // 2]
            print("The median value of your marks are", round(median, 2))
            # Placing a break statement to quit the program once average and median is found
            break
        else:
            # Placing a continue statement to go back to the beginning of the loop
            continue


markAvgMean()