age = input("Please enter your age: ")

if age <= 2:
    print "The price of your ticket is free"
elif age >=3 and age <= 13:
    print "The price of your ticket is $8.99"
elif age >= 14 and age <= 64:
    print "The price of your ticket is $12.50"
elif age >=65:
    print "The price of your ticket is $9.50"