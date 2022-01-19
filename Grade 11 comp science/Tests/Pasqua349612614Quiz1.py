#Getting the field size
size = int(input("Enter size:"))
#Getting the text entered from the user
text = input("Enter text:")

#Making the text print out once by using a for loop
for t in range(1):
    #Printing X's and multiplying them by the size entered by the user
    print("X"*size)
    print("X"*size)
    print("X"* size)
    #Checking to see if size is a even number
    if size % 2 == 0:
        #Printing spaces around the text
        print("X"*2,"     ","X"*3)
        #Printing X's with spaces around the text
        print("X"*2,"  "+(text)+" ","X"*3)
        print("X"*2,"     ","X"*3)
    #Checking to see is size is an odd number
    elif size % 2 != 0:
        #Printing spaces around the text
        print("X"*3,"     ","X"*3)
        #Printing X's with spaces around the text
        print("X"*3,"  "+(text)+" ","X"*3)
        print("X"*3,"     ","X"*3)
    print("X"*size)
    print("X"*size)
    print("X"*size)
    print("X"*size)