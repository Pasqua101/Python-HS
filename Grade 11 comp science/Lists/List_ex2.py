"""num = [2,4,6,8,10,12,14,16]

#Making a new list for multiplied numbers in list
mult_num = [2*2, 4*2, 6*2, 8*2, 10*2, 12*2, 14*2, 16*2]
print(mult_num)

#Extension A
#Getting sum of numbers in the list
num = sum(num)
#Total amount of numbers in list
total_num = 8
#Finding average of numbers i the list
average = num/total_num
print (average)

#Extension B

average_multi = (72*2)/total_num
print (average_multi)"""

#Better way of first part of the question

num1 = [2,4,6,8,10,12,14,16]
num2 = []

for i in num1:
    num2.append(i*2)
print(num2)