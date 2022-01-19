#Question 1
"""while True:
    num1 = input("Please enter a odd or even number from 1-10: ")
    num1 = num1/2
    if num1 == 2 or num1 == 4: 
        print "Even"
        break
    if num1 == 0:
        print "I'm sorry, that number can neither be odd or even"
        break
    else:
        print "Odd"
        break"""

#Question 2
"""while True:
    num1 = input("Please enter a number <type 0 to end>: ")
    if num1 == 0:
        print "Total",num1
        break
    num2 = input("Please enter another number <type 0 to end ")
    if num2 == 0:
        print "Total",num1 + num2
        break
    num3 = input("Please enter another number ")
    print "Total",num1 + num2 + num3
    break"""

#Question 3
"""while True:
    budget = input("Please enter your budget: ")
    cost1 = input("Please enter the cost of your item: ")
    budget = budget-cost1
    print "You have $",budget,"remaining"
    if budget == 0:
        print "You ran out of money"
        break
    cost2 = input("Please enter the cost of your next item: ") 
    budget = budget-cost2
    print  "You have $",budget,"remaining"
    if budget == 0:
        print "You ran out of money"
        break"""
        
#Question 4 
"""while True:    
    mark1 = input("Please input a mark")
    mark2 = input("Please enter another mark ")
    mark3 = input("Please enter one another mark")
    mark4 = input("Please enter one another mark, <type done to end>")
    hmark = mark1 < mark2 or mark1 > mark2
    himark = mark3 < mark4 or mark3 > mark4
    if mark1 == "done":
        break
if hmark > himark:
    print "The highest mark is",hmark
elif hmark < himark:
    print "The highest mark is",himark"""