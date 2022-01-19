#Question 1
"""age = input("Please enter your age.")
name = raw_input("Please enter your name.")

#Subtract current year by age then add 100 
year = 2019 - age + 100
print "In",year,"you will turn 100 years old",name

#Extension a)
num1 = input("Please enter a number")

print num1*("In",year,"you will turn 100 years old",name)

#Extension b)
num1*"\n In",year,"you will turn 100 years old",name"""

#Question 2
"""num1 = input("Please enter a number")

if num1 %2 == 0:
    print "This is a even number"

elif num1 %2 != 0:
    print "This is a odd number"
#Extension a)    
if num1 % 4 == 0:
    print "This is a multiple of 4"
    
#Extension b)
num = input("Please enter a number")
check = input("Please enter another number to divide it by")

if num % check == 0:
    print "This is a even number"
    
elif num % check != 0:
    print "This is a odd number"""
    
#Question 3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

for x in a:
    if x < 5:
        print x
#Extension a)
for x in a:    
    if x < 5:
        new_list.append(x)
        print new_list
#Extension b) 
print([i for i in a if i < 5])

#Extension c)
num = int(input("Please enter a number: "))
for i in a:
    if i < num:
        print(i)
       

