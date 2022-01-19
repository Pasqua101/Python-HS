#Question 1
"""print 1
print 2 
print 3
print 4 
print 5"""

x = 1

#Question 2

"""while x <= 10:
    print x
    x +=1 #x = x + 1"""

#or

"""while x < 10:
    x += 1
    print x"""

#or 

"""while x < 11:
    print x 
    x += 1"""
    
#or

"""while x <= 10:
    x += 1
    print x"""


#loop.py 
"""while x < 20:
    x = x+1
    print x """
    
#loop2.py

"""name = ""
while name != "end":
    name = raw_input("Enter name:<end to exit>")
    print "Hello",name"""
    
#loop3.py

# loop3.py
"""while True:
    name = raw_input("Enter name: <end to exit>")
    if name == "end":
        break
    #end if
        print "Hello",name 
    #end while 
print "The code has ended"""

#loop4.py
# enter marks (out of 100) until -1 is entered and display the number of
# marks and the average of all the marks.
"""count = 0
total = 0
while True:
    mark = input("Enter a mark (0-100) <-1 to exit> ")
    if mark == -1:
        break
    count += 1
    total += mark
print "There were", count, "marks"
print "The average is", total / count # float(total) / count"""