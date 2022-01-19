print("Welcome to the 2019 elections. Please choose a candidate from one of the shown numbers.")

print("1 = Justin Trudeau")
print("2 = Andrew Scheer")
print("3 = Jagmeet Singh")
print("4 = Theresa May")

vote = 0
trudeau = 0.0
scheer = 0.0
singh = 0.0
may = 0.0

while vote == 0:
    choice = int(input("Enter a vote(Type 0 when you are done voting)"))
    if choice == 1:
        trudeau +=1
    elif choice == 2:
        scheer +=1
    elif choice == 3:
        singh +=1
    elif choice == 4:
        may +=1
    elif choice == 0:
        break
    else:
        print("This is an invalid vote, please enter another vote.")

if trudeau > scheer and trudeau > singh and trudeau > may:
    print ("Justin Trudeau won the election")
elif scheer > trudeau and scheer > singh and scheer > may:
    print ("Andrew Scheer won the election")
elif singh > trudeau and singh > scheer and singh > may:
    print ("Jagmeet Singh won the election")
elif may > trudeau and may > scheer and may > singh:
    print ("Theresa May won the election")
    
print("Justin Truedeau earned", str(round(trudeau / (scheer + singh + may)*100.0, 2)) + "% of national votes")
print("Andrew Scheer earned", str(round(scheer / (trudeau + singh + may)*100.0, 2)) + "% of national votes")
print("Jagmeet Singh earned", str(round(singh / (scheer + trudeau+ may)*100.0, 2)) + "% of national votes")
print("Theresa May earned", str(round(may / (scheer + singh + trudeau)*100.0, 2)) + "% of national votes")
