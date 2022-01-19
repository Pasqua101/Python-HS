kids = []
weeds = []
data = []

loopnumber = input("How many of your nieces and nephews pulled weeds?")
for x in range(1,loopnumber + 1):
    name = "What is the name of child loopnumber " + str(x) + "?"
    kids.append(raw_input(name))
    weeds.append(input("How many weeds did they pull?"))
loopnum = 0

for k in kids:
    data.append(str(k) + " pulled" + str(weeds[loopnum:loopnum + 1]) + " weed(s)")
    loopnum += 1
    
for d in data:
    print d
total = float(sum(weeds))
loopnum = 0

for w in weeds:
    kid = kids[loopnum:loopnum + 1]
    w = float(w)
    print str(kid), "pulled", str(round((w/total) * 100.0, 2)) + "% of weeds. So, they get $" + str(round((w/total) * 100.0, 2))
    loopnum += 1