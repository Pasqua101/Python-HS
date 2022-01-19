def persistance(num, count=0):
    """persistance(num) - returns the persistance of the given number"""
    if num < 10:  # Checks if it is 1 digit, if it is, automatically return 0
        return count

    next_num = 1

    while num > 0:  # Basically, this loop iterates until all the digits of the number are multiplied
        digit = num % 10  # Gives the final digit (ones column)
        next_num = next_num * digit  # Multiplies the last digit (this will multiply all digits throught the loop)
        num = num // 10  # Divides by 10, eliminating the last digit

    if next_num < 10:  # If the number is 1 digit, return the persistance (+1 because the count is added at the end, which it doesn't reach)
        return count + 1

    else:  # Recursion, go through the function again, but with new number
        num = next_num
        return persistance(num, count + 1)


num = int(input("Enter your number here: "))
print("The persistance of your number is: " + str(persistance(num)))