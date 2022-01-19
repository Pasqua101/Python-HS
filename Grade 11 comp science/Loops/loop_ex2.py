number = int(input("Please enter a number: "))

num1 = 0
num2 = 1
count = 0

if number <= 0:
    print ("Please enter a positive number")
elif number == 1:
    print ("Fibonacci sequence upto",number,":")
    print (num1)
else:
    print("Fibonacci sequence upto",number,":")
    while count < number:
        print(num1,end==',')
        nth = num1 + num2
        # update values
        num1 = num2
        num2 = nth
        count += 1