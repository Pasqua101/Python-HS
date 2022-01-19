level = ["Level 1", "Level 2", "Level 3", "Level 4"]
mark = [100,52,65,78,98,59,64]
empty = []

for i in level:
    for x in mark:
        if i == "Level 1" and (x >=50 and x <60):
            empty.append(i + " - " + str(x))
        elif i == "Level 2" and (x >=60 and x <70):
            empty.append(i + " - " + str(x))     
        elif i == "Level 3" and (x >=70 and x <80):
            empty.append(i + " - " + str(x))
        elif i == "Level 4" and (x >=80 and x <=100):
            empty.append(i + " - " + str(x))     

for y in empty:
    print y

#Not related to question but is also nested loop 
"""suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
deck = []
for s in suits:
    for v in values:
        deck.append(v + " of " + s)
print deck"""
