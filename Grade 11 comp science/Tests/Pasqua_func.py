#Importing randint from random to make my lines of code shorter
from random import randint

def boo(n_1,n_2,n_3):
    """boo(n_1,n_2,n_3): Takes in three integer parameters and returns the number that is in between the other two integers"""

    #Variable name for numbers that are randomly generated
    num_1 = int(randint(1,100))
    num_2 = int(randint(1,100))
    num_3 = int(randint(1,100))

    #This loop would've been meant for determining the position of n_2
    for n_2 in range(1):
        #Determining position for num_1
        if num_1 >= num_2 and num_1 <= num_3:
            return num_2

        #determining position for num_2
        elif num_2 >= num_1 and num_2 <= num_3:
            return num_2

        # determining position for num_3
        elif num_3 >= num_1 and num_3 <= num_2:
            return n_2

    # This loop would've been meant for determining the position of n_1
    for n_1 in range(1):
        if num_1 <= num_2 and num_1 <= num_3:
            return num_1

        if num_2 <= num_1 and num_2 < num_3:
            return num_1

        if num_3 <= num_1 and num_3 < num_2:
            return num_1

    # This loop would've been meant for determining the position of n_3
    for n_3 in range(1):
        if num_1 >= num_2 and num_1 >= num_3:
            return num_3

        if num_2 >= num_1 and num_2 >= num_3:
            return num_3

        if num_3 >= num_1 and num_3 >= num_2:
            return num_3


#At the end of my code it would've printed out all the numbers in order from lowest to greatest. However, it only prints out one number. Which I don't know if it's the middle number.
print (boo(1,2,3))





