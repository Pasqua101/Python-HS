count = 0 
total = 0
while True:
    mark = input("Enter a mark (0-100) <-1 to exit>")
    if mark == -1:
        break
    count +=1
    total += mark 
    
print "There were",count,"marks"
print "The average is",total/count #float(total) / count