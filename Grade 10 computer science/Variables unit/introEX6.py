User = raw_input("Hello user, please enter your name: ")
number_of_people = input("How many guest are attending this party?")
pizza = raw_input("What kind of pizza are you ordering?")
slices = input("How many slices of pizza are you ordering?")
print "option 1:",slices / number_of_people,"pizza slices per guest, with a remainder of",slices % number_of_people," slices of", pizza
print "option 2:",slices / float(number_of_people),"slices of",pizza,"per guest"
option = raw_input("Please choose an option:")
print "Thank you",User,"for choosing",option,"enjoy your meal!"