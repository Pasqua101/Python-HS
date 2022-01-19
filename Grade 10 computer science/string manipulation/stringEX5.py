string = raw_input("Please enter something:")
feildsize = input("Please enter the field size:")
number = (feildsize - (len(string)) / 2)
print (number * (".")) + string + (number * ("."))