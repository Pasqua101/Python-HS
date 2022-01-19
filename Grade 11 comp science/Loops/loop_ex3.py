divisors = []

num = int(input("Please enter a number:"))
for n in range(1, num + 1):
    if num%n == 0:
        divisors.append(n)
divisors = str(divisors)
divisors = divisors[1:-1]
print("These are your divisors:", divisors)