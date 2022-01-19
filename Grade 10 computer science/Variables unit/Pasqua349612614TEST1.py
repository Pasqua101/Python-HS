#Question 1 
name = raw_input("Hello user please enter your full name: ")
#I put in "Hello", name[-6:], because in the example, it showed that it have to output Smith. So I counted the letters in smith and put in name[-6:] 
print "Hello", name[-6:]
price = input("What is the price of your hotel room per night? ")
#I used input because input is used for numbers where as raw_input is used for words
nights = input("How many nights will you be staying? ")
discount = input("Enter your discount amount now ex. enter 0.10 for 10 percent: ")
#I had to get the user to input their discount in a decimal, because if they didn't then the user would of saved thousands of dollars.
discount1 = (price*nights)*discount
#I used this equation, because when you are calculating the discount, you need to find the total price then multiply it by the discount
tax = 1.13
print "With your discount the total price is", discount1 * tax
#I multiplied discount by tax so I could get the full price after discount.
print "You have saved",discount1,"dollars before tax" 