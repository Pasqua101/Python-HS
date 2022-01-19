#Importing math so it can help me find the distance between the points in the polygon
import math

polygon = [[1,1],[4,6],[7,0],[4,1],[0,0]]
#Finding distance between each point of the polygon by using math.sqrt and the equation  for distance
distance1 = math.sqrt((1-4)**2+(1+6)**2)
distance2 = math.sqrt((4-7)**2 + (6-0)**2)
distance3 = math.sqrt((7-4)**2 + (0-1)**2)
distance4 = math.sqrt((4-0)**2 + (1-0)**2)
distance5 = math.sqrt((0-1)**2 + (0-1)**2)
#Adding all of the distances together to get the perimeter of the polygon
perimeter_poly = (distance1 + distance2 + distance3 + distance4 + distance5)

print("Therefore, the perimeter of the polygon is",round(perimeter_poly))

#Square
square = [10,10,10,10]
#Making a variable for one side of the square
s1 = square[0]
#Finding perimeter of the square
perimeter_sqr = (4*s1)
print("Therefore, the perimeter of the square is",perimeter_sqr)

#Triangle

Triangle =[20.3,33.4,34.8]
#Making variables for each side of the triangle
s1 = Triangle[0]
s2 = Triangle[1]
s3 = Triangle[2]
#Finding perimeter of the triangle
perimeter_tri = (s1+s2+s3)
print("Therefore, the perimeter of the triangle is",perimeter_tri)

