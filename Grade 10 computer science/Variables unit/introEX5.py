x1=input('Enter your x1:')
y1=input('Enter your x2:')
x2=input('Enter your y1:')
y2=input('Enter your y2:')
import math
def calculateDistance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist 
print calculateDistance(x1, y1, x2, y2)