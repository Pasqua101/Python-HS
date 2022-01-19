#Question1 
#misc = [ 1, 2, "Word", "Time", "Google"]

#Extension a)
"""for misc in misc:
    print misc"""
#extension b) 
"""for x in reversed(misc):
    print x"""
#Extension c)
"""for misc in misc:
    print misc * 3"""    
    
#Question2
Temp = [20, 10, 25, -2, 5, 12, 21, 16, 19, 11]

#Extension a)
"""for x in Temp:
    print x,"""
#Extension b) 
for x in reversed(Temp):
    print x 
#Extension c)
"""Temp.append(45)
Temp.append(23)
Temp.append(18)
print Temp"""
#Extension d)
"""del Temp[0]
del Temp[1]
del Temp[2]
print Temp"""
#Extension e) 
#print len(Temp)
#Extension f)
"""Temp[2] = 14
print Temp"""
#Question 3
#Use question in NestedLoops_Challenges.py as a better answer 
"""Grade = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
#Extension a)
#print Grade,
#Extension b)
#for x in reversed(Grade):
    #print x 
User = input("Please enter these 10 grades")

for Grade in range(10):
    count = 1
    total = 10
    User = input("Please enter these 10 grades")
    if count == 10:
        break
    else:
        count = count +1
        continue
#Extension (c
average = total/Grade
print average"""