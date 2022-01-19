import random

fruits = ["Apple", "Cantaloupe", "Honey dew", "Pear", "Orange", "Peaches", "Grapes", "Watermelon", "Cherries", "Nectarines", "Tangarine"]
prices = ["1.50", "3.00", "2.25", "2.00", "3.50", "1.75", "1.25", "4.00", "2.95", "2.75", "1.10" ]

print "Hello, welcome to Marco's fruit salad stand.\nHere's what we offer for your salad and the prices"

for f in fruits: 
    print  fruits [random.randint(0,10)],"-", prices[random.randint(0,10)]

