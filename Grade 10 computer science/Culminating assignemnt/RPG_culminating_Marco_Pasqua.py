#importing time to show lore in a final fantasy style 
#Background music is being played through winsound
import winsound
winsound.PlaySound('C:\Users\marco\eclipse-workspace\Grade 10 computer science\Culminating assignemnt\intro.wav', winsound.SND_ASYNC)

print "Developers note. This game is in a pre-alpha and what you are playing is just a sample of what is to come.\n Although a few things need to be hanged or adjusted. I believe that this game very stable to be played with hopefully no bugs."
print "However if you do come across errors. Please tell me what I need to fix and how to do it as some of it may or a error that I wasn't able to find or by not adding variable or misusing a function.\nThis game is developed by Marco Pasqua and is a similar python remake to the original final fantasy."
print "After I have been given feedback, I will try to work on my code during free time to see if I can shorten the length of code as this was one of my main problems. I will also fix whatever other code related problems I have"
print "However, I hope you enjoy my game"
#Using time to show intro in final fantasy style
import time
    
print "The world is veilded in darkness. The wind stops"
time.sleep(3)
print "the sea is wild,"
time.sleep(3)
print "and the earth begins to rot."
time.sleep(3)
print "The people wait,"
time.sleep(3)
print "their only hope, a prophecy...."
time.sleep(3)
print "'When the world is in darkness" 
time.sleep(3)
print "Four Warriors will come....'"
time.sleep(3)
print "After a long journey, four" 
time.sleep(3)
print "young warriors arrives,"
time.sleep(3)
print "each holding an ORB"""
    
#importing random for combat
import random
    

print ("You can chose between 6 characters, but you can only have a group of 4 characters. A black mage, a white mage, a theif, a warrior, a red mage, and a monk")
    
#First character selection
while True:
    hero1 = raw_input("Please choose your first character for your party:")
    if hero1.lower() == "white mage":
        confirm = raw_input("A white mage has the ability to heal other members of your party during battle.\nAre you sure that you want to select this character?")
        if confirm.lower() == "yes":
            hero1_name = raw_input("Please create a name for your white mage")
            break
        else:
            print"Please choose a character again"
    elif hero1.lower() == "black mage":
        confirm = raw_input("You chose a Black Mage.\nAre you sure that you want to select this character? ")
        if confirm.lower() == "yes":
            hero1_name = raw_input("Please create a name for your black mage")
            break 
        else:
            print "Please choose a character again" 
    elif hero1.lower() == "theif":
        confirm = raw_input("You chose a Theif.\nAre you sure that you want to select this character? ")
        if confirm.lower() == "yes":
            print "Choose your next party member"
            break
    elif hero1.lower() == "warrior":
        confirm = raw_input("You chose a warrior.\nAre you sure that you want to select this character?")
        if confirm.lower() == "yes":
            hero1_name = raw_input("Please create a name for your warrior")
            break
        else:
            "Please choose a character again"
    elif hero1.lower() == "red mage":
        confirm = raw_input("You chose a Red mage, this character can both heal your party and damage enemies with black magic.\nAre you sure you want this character?")
        if confirm.lower() == "yes":
            hero1_name = raw_input("Please create a name for your red mage")
            break
        else:
            print"Please chose your character again"
    elif hero1.lower() == "monk":
        confirm = raw_input("You chose a monk, this character specializes in bare-knuckle combat.\nAre you sure that you want to select this character?")
        if confirm.lower() == "yes":
            #hero name
            hero1_name = raw_input("Please create a name for your monk")
            break
        else:
            print "Please choose your character again"
            
    #Second character selection
while True:
    hero2 = raw_input("Please choose your second character for your party:")
    if hero2.lower() == "white mage":
        confirm = raw_input("A white mage has the ability to heal other members of your party during battle.\nAre you sure that you want to select this character?")
        if confirm.lower() == "yes":
            #hero name
            hero2_name = raw_input("Please create a name for your white mage")
            break
        else:
            print"Please choose a character again"
    elif hero2.lower() == "black mage":
        confirm = raw_input("You chose a Black Mage.\nAre you sure that you want to select this character?")
        if confirm.lower() == "yes":
            #hero name
            hero2_name = raw_input("Please create a name for your black mage")
            break 
        else:
            print "Please chose a character again" 
    elif hero2.lower() == "theif":
        confirm = raw_input("You chose a Theif.\nAre you sure that you want to select this character?")
        if confirm.lower() == "yes":
            #hero name
            hero2_name = raw_input("Please create a name for your theif")
            break
    elif hero2.lower() == "warrior":
        confirm = raw_input("You chose a warrior, this character can use a \nAre you sure that you want to select this character?")
        if confirm.lower() == "yes":
            #hero name
            hero1_name = raw_input("Please create a name for your warrior")
            break
        else:
            "Please choose a character again"
    elif hero2.lower() == "red mage":
        confirm = raw_input("You chose a Red mage, this character can both heal your party and damage enemies with black magic.\nAre you sure that you want to select this character?")
        if confirm.lower() == "yes":
            #hero name
            hero2_name = raw_input("Please create a name for your red mage")
            break
        else:
            print"Please chose your character again"
    elif hero2.lower() == "monk":
        confirm = raw_input("You chose a monk, this character specializes in bare-knuckle combat.\nAre you sure that you want to select this character?")
        if confirm.lower() == "yes":
            #hero name
            hero2_name = raw_input("Please create a name for your monk")
            break
            
#Third character selection         
while True:
    hero3 = raw_input("Please choose your third character for your party:")
    if hero3.lower() == "white mage":
        confirm = raw_input("A white mage has the ability to heal other members of your party during battle.\nAre you sure that you want to select this character?")
        if confirm.lower() == "yes":
            #hero name
            hero3_name = raw_input("Please create a name for your white mage")
            break
        else:
            print"Please choose a character again"
    elif hero3.lower() == "black mage":
        confirm = raw_input("You chose a Black Mage, this character has the ability to damage opponents with black mage.\nAre you sure that you want to select this character?")
        if confirm.lower() == "yes":
            #hero names
            hero3_name = raw_input("Please create a name for your black mage")
            break 
        else:
            print "Please chose a character again" 
    elif hero3.lower() == "theif":
        confirm = raw_input("You chose a Theif, this character has increased speed.\nAre you sure that you want to select this character?")
        if confirm.lower() == "yes":
            #hero names
            hero3_name = raw_input("Please create a name for your theif")
            break
        else:
            print "Please choose your character again"
    elif hero3.lower() == "warrior":
        confirm = raw_input("You chose a warrior, this character can use a wide arrange of armor and weapons.\nAre you sure that you want to select this character?")
        if confirm.lower() == "yes":
            #hero names
            hero3_name = raw_input("Please create a name for your warrior")
            break
        else:
            "Please choose a character again"
    elif hero3.lower() == "red mage":
        confirm = raw_input("You chose a Red mage, this character can both heal your party and damage enemies with black magic.\nAre you sure that you want to select this character?")
        if confirm.lower() == "yes":
            #hero name
            hero3_name = raw_input("Please create a name for your red mage")
            break
        else:
            print"Please chose your character again"
    elif hero3.lower() == "monk":
        confirm = raw_input("You chose a monk, this character specializes in bare-knuckle combat.\nAre you sure that you want to select this character?")
        if confirm.lower() == "yes":
            #hero name
            hero3_name = raw_input("Please create a name for your monk")
            break
        else:
            print "Please choose your character again"
            
#Fourth character selection 
while True:
    hero4 = raw_input("Please choose your fourth character for your party:")
    if hero4.lower() == "white mage":
        confirm = raw_input("A white mage has the ability to heal other members of your party during battle\nAre you sure that you want to select this character?")
        if confirm.lower() == "yes":
            #hero names
            hero4_name = raw_input("Please create a name for your white mage")
            break
        else:
            print"Please choose a character again"
    elif hero4.lower() == "black mage":
        confirm = raw_input("You chose a Black Mage, this character has the ability to damage opponents with black mage.\nAre you sure that you want to select this character?")
        if confirm.lower() == "yes":
            #hero names
            hero4_name = raw_input("Please create a name for your black mage")
            break 
        else:
            print "Please chose a character again" 
    elif hero4.lower() == "theif":
        confirm = raw_input("You chose a Theif, this character has increased speed.\nAre you sure that you want to select this character?")
        if confirm.lower() == "yes":
            #hero names
            hero4_name = raw_input("Please create a name for your theif")
            break
    elif hero4.lower() == "warrior":
        confirm = raw_input("You chose a warrior, this character can use a wide arrange of armor and weapons.\nAre you sure that you want to select this character?")
        if confirm.lower() == "yes":
            #hero names
            hero4_name = raw_input("Please create a name for your warrior")
            break
        else:
            "Please choose a character again"
    elif hero4.lower() == "red mage":
        confirm = raw_input("You chose a Red mage, this character can both heal your party and damage enemies with black magic.\nAre you sure that you want to select this character?")
        if confirm.lower() == "yes":
            hero4_name = raw_input("Please create a name for your red mage")
            break
        else:
            print"Please chose your character again"
    elif hero4.lower() == "monk":
        confirm = raw_input("You chose a monk, this character specializes in bare-knuckle combat.\nAre you sure that you want to select this character?")
        if confirm.lower() == "yes":
            hero4_name = raw_input("Please create a name for your monk")
            break
        else:
            print "Please choose your character again"    

winsound.PlaySound(None, winsound.SND_ASYNC)

#Characters health 
health_for_hero1 = 40
health_for_hero2 = 40
health_for_hero3 = 40
health_for_hero4 = 40

#Characters health for armor so this way heros health can reset when being healed
health_for_hero1_with_armor = health_for_hero1
health_for_hero2_with_armor = health_for_hero2
health_for_hero3_with_armor = health_for_hero3
health_for_hero4_with_armor = health_for_hero4

#Putting in prices for items in blacksmith
nunchaku = 10
knife = 5
staff = 5
rapier = 10
hammer = 10
    
#Prices for Inn
Inn = 10
    
#Prices for armor store
clothes = 10 
leather_armor = 50
chain_mail = 80
    
#Prices for Magic shop
#White magic
cure = 100
dia = 100
protect = 100
blink = 100
#Black magic
fire = 100
sleep = 100
thunder = 100

#Prices for item shop
potion = 60 
phoenix_down = 250

#Inventory list for hero's with magic
hero1_magic = []
hero2_magic = []
hero3_magic = []
hero4_magic = []

#Main inventory list 
inventory = ["Potion"]

#Hero attack damage without weapons
hero1_attack = 2
hero2_attack = 2
hero3_attack = 2
hero4_attack = 2

#Making a total so user can see how much gil they spent 
total = 0    

#Players balance 
balance = 400
    
print "Your party has spawned in the town of Cornelia\nIn this town, there is a Inn, a blacksmith, a magic store, and a armor store." 
print "If you don't want to vist these places you can type leave, you can also check your party's stats and balance by typing stats"
    
    
while True:
    
    winsound.PlaySound('C:\Users\marco\eclipse-workspace\Grade 10 computer science\Culminating assignemnt\Town.wav', winsound.SND_ASYNC)
    
    weapon = ""
    
    #Healing user's characters if they died 
    if health_for_hero1 == 0 and health_for_hero2 == 0 and health_for_hero3 == 0 and health_for_hero4 == 0:
        health_for_hero1 = health_for_hero2 = health_for_hero3 = health_for_hero4 = 50 
        
        
    movement = raw_input("Where would you like to go?")
      
    if movement.lower() == "stats":
        #Showing health for heros
        print hero1.lower(),"(",hero1_name,")","Has",health_for_hero1,"hp"  
        print hero2.lower(),"(",hero2_name,")","Has",health_for_hero2,"hp"
        print hero3.lower(),"(",hero3_name,")","Has",health_for_hero3,"hp"
        print hero4.lower(),"(",hero4_name,")","Has",health_for_hero4,"hp"    
        #Showing inventory
        print "You currently have",inventory,"in your inventory"
        #Showing hero's attack damage
        print hero1,"(",hero1_name,")","Currently does",hero1_attack,"damage"
        print hero2,"(",hero2_name,")","Currently does",hero2_attack,"damage"
        print hero3,"(",hero3_name,")","Currently does",hero3_attack,"damage"
        print hero4,"(",hero4_name,")","Currently does",hero4_attack,"damage"
        
        #Showing hero1's magic spells
        if hero1.lower() == "white mage":
            print hero1,"(",hero1_name,")","Currently has",hero1_magic,"as spells"
        elif hero1.lower() == "red mage":
            print hero1,"(",hero1_name,")","Currently has",hero1_magic,"as spells"
        elif hero1.lower() == "black mage":
            print hero1,"(",hero1_name,")","Currently has",hero1_magic,"as spells"
        #If user has a hero that cannot use magic
        else:
            print"Your hero",hero1.lower(),"(",hero1_name,")", "hero1, is not able to use spells"
        
        #Showing heros2's magic spells
        if hero2.lower() == "white mage":
            print hero2.lower(),"(",hero2_name,")","Currently has",hero2_magic,"as spells"
        elif hero2.lower() == "red mage":
            print hero2.lower(),"(",hero2_name,")","Currently has",hero2_magic,"as spells"
        elif hero2.lower() == "black mage":
            print hero2.lower(),"(",hero2_name,")","Currently has",hero2_magic,"as spells"
        #If user has a hero that cannot use magic
        else:
            print"Your hero",hero2.lower(),"(",hero2_name,")", "hero2, is not able to use spells"
        #Showing health for hero3's spells
        if hero3.lower() == "white mage":
            print hero3.lower(),"(",hero3_name,")","Currently has",hero3_magic,"as spells"
        elif hero3.lower() == "red mage":
            print hero3.lower(),"(",hero3_name,")","Currently has",hero3_magic,"as spells"
        elif hero3.lower() == "black mage":
            print hero3.lower(),"(",hero3_name,")","Currently has",hero3_magic,"as spells"
        #If user has a hero that cannot use magic
        else:
            print"Your hero",hero3.lower(),"(",hero3_name,")", "hero3, is not able to use spells"
        
        #Showing hero4's magic spells
        if hero4.lower() == "white mage":
            print hero4.lower(),"(",hero4_name,")","Currently has",hero4_magic,"as spells"
        elif hero4.lower() == "red mage":
            print hero4.lower(),"(",hero4_name,")","Currently has",hero4_magic,"as spells"
        elif hero4.lower() == "black mage":
            print hero4.lower(),"(",hero4_name,")","Currently has",hero4_magic,"as spells"
        #If user has a hero that cannot use magic
        else:
            print"Your hero",hero4.lower(),"(",hero4_name,")", "hero4, is not able to use spells"
        
        #Showing how much gil a user has and how much they spent
        if balance == 0:
            print "You currently have no gil"
        else:
            print "You currently have",balance,"gil"
            print "You spent",total,"gil, so far"
         
    
    #Inn 
    while movement.lower() == "inn":
        
        winsound.PlaySound(None, winsound.SND_ASYNC)
        winsound.PlaySound('C:\Users\marco\eclipse-workspace\Grade 10 computer science\Culminating assignemnt\shops.wav', winsound.SND_ASYNC)
        
        print "At the inn, you can pay 10 gil to rest. Resting can heal your party. You currently have",balance,"gil"
        rest = raw_input("Would you like to rest?")
        if rest.lower() == "no":
            print "You are leaving the inn."
            winsound.PlaySound(None, winsound.SND_ASYNC)
            break
        
        elif rest.lower() == "yes":
            if balance < Inn:
                print "You don't have enough to sleep at the Inn"
            elif rest.lower() == "yes":
                print "You spent 10 gil but your party has fully healed"
                #Restoring health for player's characters and taking away some of their gil(money)
                balance -=  10 
                #Restoring health for hero1
            if health_for_hero1 < health_for_hero1_with_armor:
                health_for_hero1 = health_for_hero1_with_armor
                print hero1_name,"healed back to",health_for_hero1
            #If hero is at full health
            elif health_for_hero1 == health_for_hero1_with_armor:
                print hero1_name,"Did not heal because they are at full health"
                
            #restoring health for hero2
            if health_for_hero2 < health_for_hero2_with_armor:
                health_for_hero2 = health_for_hero2_with_armor
                print hero2_name,"healed back to",health_for_hero2
            #If hero is at full health
            elif health_for_hero2 == health_for_hero2_with_armor:
                print hero2_name,"Did not heal because they are at full health"
            #Restoring health for hero3
            if health_for_hero3 < health_for_hero3_with_armor:
                health_for_hero3 = health_for_hero3_with_armor
                print hero3_name,"healed back to",health_for_hero3
            #If hero is at full health
            elif health_for_hero3 == health_for_hero3_with_armor:
                print hero3_name,"Did not heal because they are at full health"
            
            #Restoring health for hero4
            if health_for_hero4 < health_for_hero4_with_armor:
                health_for_hero4 = health_for_hero4_with_armor
                print hero4_name,"healed back to",health_for_hero4
            #If hero is at full health
            elif health_for_hero4 == health_for_hero4_with_armor:
                print hero4_name,"Did not heal because they are at full health"
                winsound.PlaySound(None, winsound.SND_ASYNC)
            break
            
        
    
    #Blacksmith put into a while statement so user can buy as much as they want 
    while movement.lower() == "blacksmith":
        
        winsound.PlaySound(None, winsound.SND_ASYNC)
        winsound.PlaySound('C:\Users\marco\eclipse-workspace\Grade 10 computer science\Culminating assignemnt\shops.wav', winsound.SND_ASYNC)
        #Reseting confirm to be used in this loop
        confirm = ""
        confirm = raw_input("At the blacksmith, you can pay for weapons for your characters.\nWould you like to buy something? <Type exit to leave the store>")
        if confirm.lower() == "yes":
            weapon =  raw_input("The black smith sells, a rapier, a knife, a staff, a nunchaku, and a hammer\nWhat would you like to buy?")
        elif confirm.lower() == "exit":
            print "You are leaving the blacksmith"
            break
                
        #Nunchaku    
        if weapon.lower() == "nunchaku":
            print "That will cost 10 gil, you currently have",balance
            confirm = raw_input("Are you sure that you want to buy this?") 
            if confirm.lower() == "yes":
                if balance < staff:
                    print "You don't have enough for this item"    
            elif confirm.lower() == "yes":
                print "Your purchase was successful, you are now currently at",balance - 10,"gil"
                balance -=10
                
                #hero1 equip
                if weapon.lower() == "hero1":
                    print hero1_name,"equipped nunchaku"
                    hero1_attack +=12
                    
                #hero2 equip
                elif weapon.lower() == "hero2":
                        print hero2_name,"equipped knife"
                        hero2_attack +=12
                        
                #hero3 equip
                elif weapon.lower() == "hero3":
                    print hero3_name,"equipped nunchaku"
                    hero3_attack +=12
                    
                #hero4 equip
                elif weapon.lower() == "hero4":
                    print hero4_name,"equipped nunchaku"
                    hero4_attack +=12
            
            
            #If user doesn't want this item
            if confirm.lower() == "no":
                print "What would you like to buy instead?"
                    
        #Knife
        if weapon.lower() == "knife":
            print "That will cost 5 gil, you currently have",balance
            confirm = raw_input("Are you sure that you want to buy this?") 
            
            #If user doesn't have enough gil 
            if confirm.lower() == "yes":
                if balance < knife:
                    print "You don't have enough for this item"
            
            #If user has enough gil
            elif confirm.lower() == "yes":
                print "Your purchase was successful, you are now currently at",balance - 5,"gil"
                balance -=5
                
                #equip
                weapon = raw_input("Who do you want to learn the spell(type hero1, hero2, ect. so you can equip it for that certain hero).")
                    
                #hero1 equip
                if weapon.lower() == "hero1":
                    print hero1_name,"equipped knife"
                    hero1_attack +=5
                    
                #hero2 equip
                if weapon.lower() == "hero2":
                        print hero2_name,"equipped knife"
                        hero2_attack +=5
                        
                #hero3 equip
                if weapon.lower() == "hero3":
                    print hero3_name,"equipped knife"
                    hero3_attack +=5
                    
                #hero4 equip
                if weapon.lower() == "hero4":
                    print hero4_name,"equipped knife"
                    hero4_attack +=5
            
            
            #If user doesn't want this item
            if confirm.lower() == "no":
                print "What would you like to buy instead?"
                    
                
        #Staff   
        if weapon.lower() == "staff":
            print "That will cost 5 gil, you currently have",balance
            confirm = raw_input("Are you sure that you want to buy this?") 
            #If user doesn't have enough gil 
            if confirm.lower() == "yes":
                if balance < staff:
                    print "You don't have enough for this item"
            
            #If user has enough gil
            elif confirm.lower() == "yes":
                print "Your purchase was successful, you are now currently at",balance - 5,"gil"
                balance -=10
                
                #equip
                weapon = raw_input("Who do you want to learn the spell(type hero1, hero2, ect. so you can equip it for that certain hero).")
                    
                #hero1 equip
                if weapon.lower() == "hero1":
                    print hero1_name,"equipped staff"
                    hero1_attack +=6
                    
                #hero2 equip
                if weapon.lower() == "hero2":
                        print hero2_name,"equipped staff"
                        hero2_attack +=6
                        
                #hero3 equip
                if weapon.lower() == "hero3":
                    print hero3_name,"equipped staff"
                    hero3_attack +=6
                    
                #hero4 equip
                if weapon.lower() == "hero4":
                    print hero4_name,"equipped staff"
                    hero4_attack +=6
            
            #If user doesn't want this item 
            if confirm.lower() == "no":
                print "What would you like to buy instead?"
                    
            
        #rapier
        if weapon.lower() == "rapier":
            print "That will cost 10 gil, you currently have",balance
            confirm = raw_input("Are you sure that you want to buy this?") 
            #If user doesn't have enough gil 
            if confirm.lower() == "yes":
                if balance < rapier:
                    print "You don't have enough for this item"
            #If user has enough gil
            elif confirm.lower() == "yes":
                print "Your purchase was successful, you are now currently at",balance - 10,"gil"
                balance -=5
                
                #equip reseting so weapon can be used again
                weapon = ""
                weapon = raw_input("Who do you want to learn the spell(type hero1, hero2, ect. so you can equip it for that certain hero).")
                    
                #hero1 equip
                if weapon.lower() == "hero1":
                    print hero1_name,"equipped rapier"
                    hero1_attack +=9
                    
                #hero2 equip
                if weapon.lower() == "hero2":
                        print hero2_name,"equipped rapier"
                        hero2_attack +=9
                        
                #hero3 equip
                if weapon.lower() == "hero3":
                    print hero3_name,"equipped rapier"
                    hero3_attack +=9
                    
                #hero4 equip
                if weapon.lower() == "hero4":
                    print hero4,"equipped rapier"
                    hero4_attack +=9
            
                
            #If user doesn't want this spell    
            if confirm.lower() == "no":
                print "What would you like to buy instead?"
                    
            
        #hammer
        if weapon.lower() == "hammer":
            print "That will cost 10 gil, you currently have",balance
            confirm = ""
            confirm = raw_input("Are you sure that you want to buy this?") 
            #If user doesn't have enough gil
            if confirm.lower() == "yes":
                if balance < hammer:
                    print "You don't have enough for this item"
            #If user has enough gil
            elif confirm.lower() == "yes":
                print "Your purchase was successful, you are now currently at",balance - 10,"gil"
                balance -=10
                
                #equip
                weapon = raw_input("Who do you want to learn the spell(type hero1, hero2, ect. so you can equip it for that certain hero).")
                    
                #hero1 equip
                if weapon.lower() == "hero1":
                    print hero1_name,"equipped hammer"
                    hero1_attack +=9
                    
                #hero2 equip
                if weapon.lower() == "hero2":
                        print hero2_name,"equipped hammer"
                        hero2_attack +=9
                        
                #hero3 equip
                if weapon.lower() == "hero3":
                    print hero3_name,"equipped hammer"
                    hero3_attack +=9
                    
                #hero4 equip
                if weapon.lower() == "hero4":
                    print hero4_name,"equipped hammer"
                    hero4_attack +=9

            #If user doesn't want this spell
            if confirm.lower() == "no":
                print "What would you like to buy instead?"
                    
         
        #Armor store put into while statement so user can buy as much as they want 
        while movement.lower() == "armor store":
            
            winsound.PlaySound(None, winsound.SND_ASYNC)
            winsound.PlaySound('C:\Users\marco\eclipse-workspace\Grade 10 computer science\Culminating assignemnt\shops.wav', winsound.SND_ASYNC)
            #Have to define armor
            
            
            confirm = raw_input("At the armor store, you can pay for armor that your characters can use.\nWould you like to buy something?")
            if confirm.lower() == "yes":
                armor = raw_input("The black smith sells, a rapier, a knife, a staff, a nunchaku, and a hammer\nWhat would you like to buy?")
            
            elif confirm.lower() == "no":
                winsound.PlaySound(None, winsound.SND_ASYNC)
                break
                
            #Clothes    
            if armor.lower() == "clothes":
                print "That will cost 10 gil, you currently have",balance
                confirm = ""
                confirm = raw_input("Are you sure that you want to buy this?") 
            
                #If user doesn't have enough gil
                if confirm.lower() == "yes":
                    if balance < clothes:
                        print "You don't have enough for this item"
            #if user has enough gil
            elif confirm.lower() == "yes":
                print "Your purchase was successful, you are now currently at",balance - 10,"gil."
                balance -=10
                
                #equip
                defense = ""
                defense = raw_input("Who do you want to learn the spell(type hero1, hero2, ect. so you can equip it for that certain hero).")
                    
                #hero1 equip
                if defense.lower() == "hero1":
                    print hero1_name,"equipped clothes"
                    #Making health for hero with armor so it's easier to fully heal them 
                    health_for_hero1_with_armor +=1
                    health_for_hero1 +=1
                    print "Your character now has",health_for_hero1,"health points(hp)"
                    
                #hero2 equip
                elif defense.lower() == "hero2":
                        print hero2_name,"equipped clothes"
                        #Making health for hero with armor so it's easier to fully heal them 
                        health_for_hero2_with_armor +=1
                        health_for_hero2 +=1
                        print "Your character now has",health_for_hero1,"health points(hp)"
                        
                #hero3 equip
                elif defense.lower() == "hero3":
                    print hero3_name,"equipped clothes"
                    #Making health for hero with armor so it's easier to fully heal them 
                    health_for_hero3_with_armor +=1
                    health_for_hero3 +=1
                    print "Your character now has",health_for_hero1,"health points(hp)"
                    
                #hero4 equip
                elif defense.lower() == "hero4":
                    print hero4_name,"equipped clothes"
                    #Making health for hero with armor so it's easier to fully heal them 
                    health_for_hero4_with_armor +=1
                    health_for_hero4 +=1
                    print "Your character now has",health_for_hero1,"health points(hp)"
                
            #If user doesn't want to buy this 
            elif confirm.lower() == "no":
                print "What would you like to buy instead?"
                    
            
            #Leather armor 
            elif armor.lower() == "leather armor":
                confirm = ""
                print "That will cost 50 gil, you currently have",balance
                confirm = raw_input("Are you sure that you want to buy this?") 
                
            #If user has less than the amount of gil needed
            if confirm.lower() == "yes":
                if balance < leather_armor:
                    print "You don't have enough for this item"            
            #If user has enough gil
            elif confirm.lower() == "yes":
                balance -=50
                print "Your purchase was successful, you are now currently at",balance,"gil."
                
                
                #equip
                defense = ""
                defense = raw_input("Who do you want to learn the spell(type hero1, hero2, ect. so you can equip it for that certain hero).")
                    
                #hero1 equip
                if defense.lower() == "hero1":
                    print hero1_name,"equipped leather armor"
                    #Making health for hero with armor so it's easier to fully heal them 
                    health_for_hero1_with_armor +=4
                    health_for_hero1 +=4
                    print "Your character now has",health_for_hero1,"health points(hp)"
                    
                #hero2 equip
                elif defense.lower() == "hero2":
                        print hero2_name,"equipped leather armor"
                        #Making health for hero with armor so it's easier to fully heal them 
                        health_for_hero2_with_armor +=4
                        health_for_hero2 +=4
                        print "Your character now has",health_for_hero1,"health points(hp)"
                        
                #hero3 equip
                elif defense.lower() == "hero3":
                    print hero3_name,"equipped leather armor"
                    #Making health for hero with armor so it's easier to fully heal them 
                    health_for_hero3_with_armor +=4
                    health_for_hero3 +=4
                    print "Your character now has",health_for_hero1,"health points(hp)"
                    
                #hero4 equip
                if defense.lower() == "hero4":
                    print hero4_name,"equipped leather armor"
                    #Making health for hero with armor so it's easier to fully heal them 
                    health_for_hero4_with_armor +=4
                    health_for_hero4 +=4
                    print "Your character now has",health_for_hero1,"health points(hp)"
            
            #If user doesn't want to buy this        
            if confirm.lower() == "no":
                print "What would you like to buy"
                
            #Chain Mail  
            armor = "" 
            if armor.lower() == "chain mail":
                print "That will cost 80 gil, you currently have",balance
                confirm = ""
                confirm = raw_input("Are you sure that you want to buy this?") 
           
           #If user has less than the amount of gil needed
            if confirm.lower() == "yes":
                if balance < chain_mail:
                    print "You don't have enough for this item"
            #If user has enough gil            
            elif confirm.lower() == "yes":
                print "Your purchase was successful, you are now currently at",balance - 80,"gil."
                balance -= 80    
                
                #equip
                defense = raw_input("Who do you want to learn the spell(type hero1, hero2, ect. so you can equip it for that certain hero).")
                    
                #hero1 equip
                if defense.lower() == "hero1":
                    print hero1,"equipped chain mail"
                    #Making health for hero with armor so it's easier to fully heal them 
                    health_for_hero1_with_armor +=15
                    health_for_hero1 +=15
                    print "Your character now has",health_for_hero1,"health points(hp)"
                    
                #hero2 equip
                elif defense.lower() == "hero2":
                        print hero2,"equipped chain mail"
                        #Making health for hero with armor so it's easier to fully heal them 
                        health_for_hero2_with_armor +=15
                        health_for_hero2 +=15
                        print "Your character now has",health_for_hero1,"health points(hp)"
                        
                #hero3 equip
                elif defense.lower() == "hero3":
                    print hero3,"equipped chain mail"
                    #Making health for hero with armor so it's easier to fully heal them 
                    health_for_hero3_with_armor +=15
                    health_for_hero3 +=15
                    print "Your character now has",health_for_hero1,"health points(hp)"
                    
                #hero4 equip
                elif defense.lower() == "hero4":
                    print hero4,"equipped chain mail"
                    #Making health for hero with armor so it's easier to fully heal them 
                    health_for_hero4_with_armor +=15
                    health_for_hero4 +=15
                    print "Your character now has",health_for_hero1,"health points(hp)"
            
            #If user doesn't want this
            elif confirm.lower() == "no":
                print "What would you like to buy?"
                    
        #Magic store put into while statement so user can buy what they want
    while movement.lower() == "magic store":
        winsound.PlaySound(None, winsound.SND_ASYNC)
        winsound.PlaySound('C:\Users\marco\eclipse-workspace\Grade 10 computer science\Culminating assignemnt\shops.wav', winsound.SND_ASYNC)
        #Making players decide between different catagories of magic
        category = raw_input("The magic store sells, White magic and Black magic items.\nWhat category would you like to see? <You can type exit to leave>")
        #Leaving the store
        if category.lower() == "exit":
            print "You are leaving the magic store"
            break
    
            
        #Black magic put into a while loop so if they mess up they won't go back to the begining of the while statement
        while category.lower() == "black magic":
            print "The black Magic items that the are sold is fire, sleep and thunder"
            confirm = ""
            magic = ""
            
            confirm = raw_input("Would you like to buy something?<Type exit to look at a different category>")
            if confirm.lower() == "yes":
                magic = raw_input("What would you like to buy?")
            elif confirm.lower() == "no":
                print "What category would you like to look at?"
                break
                
            #Fire
            if magic.lower() == "fire":
                print "That will cost 100 gil, you currently have",balance,"gil"
                confirm = raw_input("Are you sure you want to buy this?")
                
                #If user has enough gil
                if confirm.lower() == "yes":
                    print "Your purchase was successful, you are now currently at",balance - 100,"gil."
                    balance -=100
                    
                    #equip 
                    spell = raw_input("Who do you want to learn the spell(type hero1, hero2, ect. so you can equip it for that certain hero. But mages can only learn spells)")
                    
                    #hero1 equip
                    if spell.lower() == "hero1":
                        if hero1.lower() == "red mage" or hero1.lower() == "black mage":
                            print hero1_name,"learned fire"
                            hero1_magic.append("Fire")
                            print "Here's what spells you have for this hero",hero1_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower() == "yes":
                                print "\n"
                            elif confirm.lower() == "no":
                                break
                    
                        #If user doesn't have a mage
                        elif spell.lower() == "hero1":
                            if hero1.lower() == "monk" or hero1.lower() == "white mage" or hero1.lower() == "warrior":
                                print "This spell doesn't work for that hero, you are getting refunded"
                                balance += 100
                                print "you are still at",balance,"gil"
                    
                    #hero2 equip
                    elif spell.lower() == "hero2":
                        if hero2.lower() == "red mage" or hero2.lower() == "black mage":
                            print hero2_name,"learned fire"
                            hero2_magic.append("Fire")
                            print "Here's what spells you have for this hero",hero2_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower() == "yes":
                                print "\n"
                            elif confirm.lower() == "no":
                                break
                            
                    #If user doesn't have a mage
                    elif spell.lower() == "hero2":
                        if hero2.lower() == "black mage" or hero2.lower() == "monk" or hero2.lower() == "warrior":
                            print "This spell doesn't work for that hero, you are getting refunded"
                            balance += 100
                            print "you are still at",balance,"gil"
                                
                    #hero3 equip
                    elif spell.lower() == "hero3":
                        if hero3.lower() == "red mage" or hero3.lower() == "black mage":
                            print hero3_name,"learned fire"
                            hero3_magic.append("Fire")
                            print "Here's what spells you have for this hero",hero3_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower()== "yes":
                                print "\n"
                            elif confirm.lower() == "no":
                                break
                    
                    #If user doesn't have a mage
                    elif spell.lower() == "hero3":
                        if hero3.lower() == "white mage" or hero3.lower() == "monk" or hero3.lower() == "warrior":
                            print "This spell doesn't work for that hero, you are getting refunded"
                            balance += 100
                            print "you are still at",balance,"gil"
                    
                    #hero4 equip
                    elif spell.lower() == "hero4":
                        if hero4.lower() == "red mage" or hero4.lower() == "black mage":
                            print hero4_name,"learned fire"
                            hero4_magic.append("Fire")
                            print "Here's what spells you have for this hero",hero4_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower() == "yes":
                                print "\n"
                            elif confirm.lower() == "no":
                                break
                    #If user doesn't have a mage
                    elif spell.lower() == "hero4":
                        if hero4.lower() == "white mage" or hero4.lower() == "monk" or hero4.lower() == "warrior":
                            print "This spell doesn't work for that hero, you are getting refunded"
                            balance += 100
                            print "you are still at",balance,"gil"  
                
                #If user has less than the amount of gil needed
                elif confirm.lower() == "yes":
                    if balance < fire:
                        print "You don't have enough gil for any magic spells"         
                
                #If user doesn't want to pay for the spell
                elif confirm.lower() == "no":
                    print "What would you like to buy"
           
            #Sleep
            elif magic.lower() == "sleep":
                print "That will cost 100 gil, you currently have",balance,"gil"
                confirm = raw_input("Are you sure you want to buy this?")
               
                #If user has enough gil needed
                if confirm.lower() == "yes":
                    print "Your purchase was successful, you are now currently at",balance - 100,"gil."
                    balance -=100
                    
                    #equip
                    spell = raw_input("Who do you want to learn the spell(type hero1, hero2, ect. so you can equip it for that certain hero. But mages can only learn spells)")
                    
                    #hero1 equip
                    if spell.lower() == "hero1":
                        if hero1.lower() == "red mage" or hero1.lower() == "black mage":
                            print hero1_name,"learned sleep"
                            hero1_magic.append("Sleep")
                            print "Here's what spells you have for this hero",hero1_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower() == "yes":
                                print "\n"
                            elif confirm.lower() == "no":
                                break
                    
                        #If user doesn't have a mage
                        elif spell.lower() == "hero1":
                            if hero1.lower() == "monk" or hero1.lower() == "white mage" or hero1.lower() == "warrior":
                                print "This spell doesn't work for that hero, you are getting refunded"
                                balance += 100
                                print "you are still at",balance,"gil"
                    
                    #hero2 equip
                    elif spell.lower() == "hero2":
                        if hero2.lower() == "red mage" or hero2.lower() == "black mage":
                            print hero2_name,"learned sleep"
                            hero2_magic.append("Sleep")
                            print "Here's what spells you have for this hero",hero2_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower() == "yes":
                                print "\n"
                            elif confirm.lower == "no":
                                break
                            break
                    #If user doesn't have a mage
                    elif spell.lower() == "hero2":
                        if hero2.lower() == "black mage" or hero2.lower() == "monk" or hero2.lower() == "warrior":
                            print "This spell doesn't work for that hero, you are getting refunded"
                            balance += 100
                            print "you are still at",balance,"gil"
                                
                    #hero3 equip
                    elif spell.lower() == "hero3":
                        if hero3.lower() == "red mage" or hero3.lower() == "black mage":
                            print hero3_name,"learned sleep"
                            hero3_magic.append("Sleep")
                            print "Here's what spells you have for this hero",hero3_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower()== "yes":
                                print "\n"
                            elif confirm == "No" or confirm == "no":
                                break
                    
                    #If user doesn't have a mage
                    elif spell.lower() == "hero3":
                        if hero3.lower() == "white mage" or hero2.lower() == "monk" or hero2.lower() == "warrior":
                            print "This spell doesn't work for that hero, you are getting refunded"
                            balance += 100
                            print "you are still at",balance,"gil"
                    
                    #hero4 equip
                    elif spell.lower() == "hero4":
                        if hero4.lower() == "red mage" or hero4.lower() == "black mage":
                            print hero4_name,"learned sleep"
                            hero4_magic.append("Sleep")
                            print "Here's what spells you have for this hero",hero4_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower() == "yes":
                                print "\n"
                            elif confirm.lower() == "no":
                                break
                    #If user doesn't have a mage
                    elif spell.lower() == "hero4":
                        if hero4.lower() == "white mage" or hero2.lower() == "monk" or hero2.lower() == "warrior":
                            print "This spell doesn't work for that hero, you are getting refunded"
                            balance += 100
                            print "you are still at",balance,"gil"
                    
                #If user has less than the amount of gil needed
                elif confirm.lower() == "yes":
                    if balance < sleep:
                        print "You don't have enough gil for any magic spells"    
                
                elif confirm.lower() == "no":
                    print "What would you like to buy?"
                
            
            
            #Thunder
            elif magic == "Thunder" or magic == "thunder":
                print "That will cost 100 gil, you currently have",balance,"gil"
                confirm = raw_input("Are you sure you want to buy this?")
                
                #If user has enough gil
                if confirm == "Yes" or confirm == "yes":
                    print "Your purchase was successful, you are now currently at",balance - 100,"gil."
                    balance = balance - 100
                    
                    #equip 
                    spell = raw_input("Who do you want to learn the spell(type hero1, hero2, ect. so you can equip it for that certain hero. But mages can only learn spells)")
                    
                    #hero1 equip
                    if spell.lower() == "hero1":
                        if hero1.lower() == "red mage" or hero1.lower() == "black mage":
                            print hero1_name,"learned thunder"
                            hero1_magic.append("Thunder")
                            print "Here's what spells you have for this hero",hero1_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower() == "yes":
                                print "\n"
                            elif confirm.lower() == "no":
                                break
                    
                        #If user doesn't have a mage
                        elif spell.lower() == "hero1":
                            if hero1.lower() == "monk" or hero1.lower() == "white mage" or hero1.lower() == "warrior":
                                print "This spell doesn't work for that hero, you are getting refunded"
                                balance += 100
                                print "you are still at",balance,"gil"
                    
                    #hero2 equip
                    elif spell.lower() == "hero2":
                        if hero2.lower() == "red mage" or hero2.lower() == "black mage":
                            print hero2_name,"learned thunder"
                            hero2_magic.append("Thunder")
                            print "Here's what spells you have for this hero",hero2_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower() == "yes":
                                print "\n"
                            elif confirm.lower == "no":
                                break
                            break
                    #If user doesn't have a mage
                    elif spell.lower() == "hero2":
                        if hero2.lower() == "black mage" or hero2.lower() == "monk" or hero2.lower() == "warrior":
                            print "This spell doesn't work for that hero, you are getting refunded"
                            balance += 100
                            print "you are still at",balance,"gil"
                                
                    #hero3 equip
                    elif spell.lower() == "hero3":
                        if hero3.lower() == "red mage" or hero3.lower() == "black mage":
                            print hero3_name,"learned thunder"
                            hero3_magic.append("Thunder")
                            print "Here's what spells you have for this hero",hero3_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower()== "yes":
                                print "\n"
                            elif confirm == "No" or confirm == "no":
                                break
                    
                    #If user doesn't have a mage
                    elif spell.lower() == "hero3":
                        if hero3.lower() == "white mage" or hero3.lower() == "monk" or hero3.lower() == "warrior":
                            print "This spell doesn't work for that hero, you are getting refunded"
                            balance += 100
                            print "you are still at",balance,"gil"
                    
                    #hero4 equip
                    elif spell.lower() == "hero4":
                        if hero4.lower() == "red mage" or hero4.lower() == "black mage":
                            print hero4_name,"learned thunder"
                            hero4_magic.append("Thunder")
                            print "Here's what spells you have for this hero",hero4_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower() == "yes":
                                print "\n"
                            elif confirm.lower() == "no":
                                break
                    #If user doesn't have a mage
                    elif spell.lower() == "hero4":
                        if hero4.lower() == "white mage" or hero4.lower() == "monk" or hero4.lower() == "warrior":
                            print "This spell doesn't work for that hero, you are getting refunded"
                            balance += 100
                            print "you are still at",balance,"gil"
                    
                #If user has less than the amount of gil needed
                elif confirm.lower() == "yes":
                    if balance < thunder:
                        print "You don't have enough gil for any magic spells"    
                
                #If user doesn't want to pay for the spell    
                elif confirm.lower() == "no":
                    print "What would you like to buy"
                    
        #White magic
        while category.lower() == "white magic":
            print "The white Magic items that the are sold is cure, dia, protect, and blink"
            #if the user puts in no for the confirm, it will print out 2 print statements this can be stopped by typing in no again
            confirm = ""
            magic = ""
            confirm = raw_input("Would you like to buy something?<Type exit to leave>")
            
            if confirm.lower() == "yes":
                magic = raw_input("What would you like to buy?")
                
                #Cure
                if magic.lower() == "cure":
                    print "That will cost 100 gil, you currently have",balance,"gil"
                    confirm = raw_input("Are you sure you want to buy this?")
                    spell = raw_input("Who do you want to learn the spell(type hero1, hero2, ect. so you can equip it for that certain hero. But mages can only learn spells)")
                    
                    #hero1 equip
                    if spell == "hero1":
                        if hero1.lower() == "red mage" or hero1.lower() == "white mage":
                            print hero1_name,"learned cure"
                            hero1_magic.append("Cure")
                            print "Here's what spells you have for this hero",hero1_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower() == "yes":
                                print "\n"
                            elif confirm.lower() == "no":
                                break
                    
                        #If user doesn't have a mage
                        elif spell == "hero1":
                            if hero1.lower() == "monk" or hero1.lower() == "black mage" or hero1.lower() == "warrior":
                                print "This spell doesn't work for that hero, you are getting refunded"
                                balance += 100
                                print "you are still at",balance,"gil"
                    
                    #hero2 equip
                    elif spell == "hero2":
                        if hero2.lower() == "red mage" or hero2.lower() == "white mage":
                            print hero2_name,"learned cure"
                            hero2_magic.append("Cure")
                            print "Here's what spells you have for this hero",hero2_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower() == "yes":
                                print "\n"
                            elif confirm.lower == "no":
                                break
                            break
                    #If user doesn't have a mage
                    elif spell.lower() == "hero2":
                        if hero2.lower() == "black mage" or hero2.lower() == "monk" or hero2.lower() == "warrior":
                            print "This spell doesn't work for that hero, you are getting refunded"
                            balance += 100
                            print "you are still at",balance,"gil"
                    
                                
                    #hero3 equip
                    elif spell == "hero3":
                        if hero3.lower() == "red mage" or hero3.lower() == "white mage":
                            print hero3_name,"learned cure"
                            hero3_magic.append("Cure")
                            print "Here's what spells you have for this hero",hero3_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower()== "yes":
                                print "\n"
                            elif confirm == "No" or confirm == "no":
                                break
                    
                    #If user doesn't have a mage
                    elif spell == "hero3":
                        if hero3.lower() == "black mage" or hero2.lower() == "monk" or hero2.lower() == "warrior":
                            print "This spell doesn't work for that hero, you are getting refunded"
                            balance += 100
                            print "you are still at",balance,"gil"
                    
                    #hero4 equip
                    elif spell.lower() == "hero4":
                        if hero4.lower() == "red mage" or hero4.lower() == "white mage":
                            print hero4_name,"learned cure"
                            hero4_magic.append("Cure")
                            print "Here's what spells you have for this hero",hero4_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower() == "yes":
                                print "\n"
                            elif confirm.lower() == "no":
                                break
                    #If user doesn't have a mage
                    elif spell.lower() == "hero4":
                        if hero4.lower() == "black mage" or hero4.lower() == "monk" or hero4.lower() == "warrior":
                            print "This spell doesn't work for that hero, you are getting refunded"
                            balance += 100
                            print "you are still at",balance,"gil"
                            
            #If user has less than the amount of gil needed
            elif confirm.lower() == "yes":
                if balance < cure:
                    print "You don't have enough gil for any magic spells"
            
            
            
            #break so user can choose a different category 
            if confirm.lower() == "exit":
                break
            
            #Dia
            if magic.lower() == "dia":
                print "That will cost 100 gil, you currently have",balance,"gil"
                confirm = raw_input("Are you sure you want to buy this?")
            
                #If user has enough gil 
                if confirm.lower() == "yes":
                    print "Your purchase was successful, you are now currently at",balance - 100,"gil."
                    balance -=100
                
                    #equip
                    spell = raw_input("Who do you want to learn the spell(type hero1, hero2, ect. so you can equip it for that certain hero. But mages can only learn spells)")
                    
                    #hero1 equip
                    if spell.lower() == "hero1":
                        if hero1.lower() == "red mage" or hero1.lower() == "white mage":
                            print hero1_name,"learned dia"
                            hero1_magic.append("Dia")
                            print "Here's what spells you have for this hero",hero1_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower() == "yes":
                                print "\n"
                            elif confirm.lower() == "no":
                                break
                    
                        #If user doesn't have a mage
                        elif spell.lower() == "hero1":
                            if hero1.lower() == "monk" or hero1.lower() == "black mage" or hero1.lower() == "warrior":
                                print "This spell doesn't work for that hero, you are getting refunded"
                                balance += 100
                                print "you are still at",balance,"gil"
                    
                    #hero2 equip
                    elif spell.lower() == "hero2":
                        if hero2.lower() == "red mage" or hero2.lower() == "white mage":
                            print hero2_name,"learned dia"
                            hero2_magic.append("Dia")
                            print "Here's what spells you have for this hero",hero2_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower() == "yes":
                                print "\n"
                            elif confirm.lower() == "no":
                                break
                            break
                    #If user doesn't have a mage
                    elif spell.lower() == "hero2":
                        if hero2.lower() == "black mage" or hero2.lower() == "monk" or hero2.lower() == "warrior":
                            print "This spell doesn't work for that hero, you are getting refunded"
                            balance += 100
                            print "you are still at",balance,"gil"
                    
                                
                    #hero3 equip
                    elif spell.lower() == "hero3":
                        if hero3.lower() == "red mage" or hero3.lower() == "white mage":
                            print hero3_name,"learned dia"
                            hero3_magic.append("Dia")
                            print "Here's what spells you have for this hero",hero3_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower()== "yes":
                                print "\n"
                            elif confirm.lower() == "no":
                                break
                    
                    #If user doesn't have a mage
                    elif spell.lower() == "hero3":
                        if hero3.lower() == "black mage" or hero2.lower() == "monk" or hero2.lower() == "warrior":
                            print "This spell doesn't work for that hero, you are getting refunded"
                            balance += 100
                            print "you are still at",balance,"gil"
                            
                    #hero4 equip
                    elif spell.lower() == "hero4":
                        if hero4.lower() == "red mage" or hero4.lower() == "white mage":
                            print hero4_name,"learned dia"
                            hero4_magic.append("Dia")
                            print "Here's what spells you have for this hero",hero4_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower() == "yes":
                                print "\n"
                            elif confirm.lower() == "no":
                                break
                    #If user doesn't have a mage
                    elif spell.lower() == "hero4":
                        if hero4.lower() == "black mage" or hero2.lower() == "monk" or hero2.lower() == "warrior":
                            print "This spell doesn't work for that hero, you are getting refunded"
                            balance += 100
                            print "you are still at",balance,"gil"
            
            
            #If user has less than the amount of gil needed
            elif confirm.lower() == "yes":
                if balance < dia:
                    print "You don't have enough gil for any magic spells"
            
            #If user doesn't want to buy the spell  
            if confirm.lower() == "no":
                print "What would you like to buy"
                
            #protect
            if magic.lower() == "protect":
                print "That will cost 100 gil, you currently have",balance,"gil"
                confirm = raw_input("Are you sure you want to buy this?")
            
                #If user has enough gil
                if confirm.lower() == "yes":
                    print "Your purchase was successful, you are now currently at",balance - 100,"gil."
                    balance -=100
                    #equip
                    spell = raw_input("Who do you want to learn the spell(type hero1, hero2, ect. so you can equip it for that certain hero. But mages can only learn spells)")
                    
                    #hero1 equip
                    if spell.lower() == "hero1":
                        if hero1.lower() == "red mage" or hero1.lower() == "white mage":
                            print hero1_name,"learned protect"
                            hero1_magic.append("protect")
                            print "Here's what spells you have for this hero",hero1_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower() == "yes":
                                print "\n"
                            elif confirm.lower() == "no":
                                break
                    
                        #If user doesn't have a mage
                        elif spell.lower() == "hero1":
                            if hero1.lower() == "monk" or hero1.lower() == "black mage" or hero1.lower() == "warrior":
                                print "This spell doesn't work for that hero, you are getting refunded"
                                balance += 100
                                print "you are still at",balance,"gil"
                    
                    #hero2 equip
                    elif spell.lower() == "hero2":
                        if hero2.lower() == "red mage" or hero2.lower() == "white mage":
                            print hero2_name,"learned protect"
                            hero2_magic.append("Protect")
                            print "Here's what spells you have for this hero",hero2_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower() == "yes":
                                print "\n"
                            elif confirm.lower() == "no":
                                break
                            break
                    #If user doesn't have a mage
                    elif spell.lower() == "hero2":
                        if hero2.lower() == "black mage" or hero2.lower() == "monk" or hero2.lower() == "warrior":
                            print "This spell doesn't work for that hero, you are getting refunded"
                            balance += 100
                            print "you are still at",balance,"gil"
                                
                    #hero3 equip
                    elif spell.lower() == "hero3":
                        if hero3.lower() == "red mage" or hero3.lower() == "white mage":
                            print hero3_name,"learned protect"
                            hero3_magic.append("Protect")
                            print "Here's what spells you have for this hero",hero3_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower()== "yes":
                                print "\n"
                            elif confirm == "No" or confirm == "no":
                                break
                    
                    #If user doesn't have a mage
                    elif spell.lower() == "hero3":
                        if hero3.lower() == "black mage" or hero2.lower() == "monk" or hero2.lower() == "warrior":
                            print "This spell doesn't work for that hero, you are getting refunded"
                            balance += 100
                            print "you are still at",balance,"gil"
                    
                    #hero4 equip
                    elif spell.lower() == "hero4":
                        if hero4.lower() == "red mage" or hero4.lower() == "white mage":
                            print hero4_name,"learned protect"
                            hero4_magic.append("Protect")
                            print "Here's what spells you have for this hero",hero4_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower() == "yes":
                                print "\n"
                            elif confirm.lower() == "no":
                                break
                    #If user doesn't have a mage
                    elif spell.lower() == "hero4":
                        if hero4.lower() == "black mage" or hero2.lower() == "monk" or hero2.lower() == "warrior":
                            print "This spell doesn't work for that hero, you are getting refunded"
                            balance += 100
                            print "you are still at",balance,"gil"
                        
            #If user has less than the amount of gil needed
            elif confirm.lower() == "yes":
                if balance < protect:
                    print "You don't have enough gil for any magic spells"
            
            #If user doesn't want to buy the spell
            elif confirm.lower() == "no":
                print "What would you like to buy"
                
            #Blink
            if magic.lower() == "blink":
                print "That will cost 100 gil, you currently have",balance,"gil"
                confirm = raw_input("Are you sure you want to buy this?")
            
                #If user has enough gil
                if confirm.lower() == "yes":
                    print "Your purchase was successful, you are now currently at",balance - 100,"gil."
                    balance -=100
                
                    #equip
                    spell = raw_input("Who do you want to learn the spell(type hero1, hero2, ect. so you can equip it for that certain hero. But mages can only learn spells)")
                    
                    #hero1 equip
                    if spell.lower() == "hero1":
                        if hero1.lower() == "red mage" or hero1.lower() == "white mage":
                            print hero1_name,"learned blink"
                            hero1_magic.append("Blink")
                            print "Here's what spells you have for this hero",hero1_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower() == "yes":
                                print "\n"
                            elif confirm.lower() == "no":
                                break
                    
                        #If user doesn't have a mage
                        elif spell == "hero1":
                            if hero1.lower() == "monk" or hero1.lower() == "black mage" or hero1.lower() == "warrior":
                                print "This spell doesn't work for that hero, you are getting refunded"
                                balance += 100
                                print "you are still at",balance,"gil"
                    
                    #hero2 equip
                    elif spell == "hero2":
                        if hero2.lower() == "red mage" or hero2.lower() == "white mage":
                            print hero2_name,"learned blink"
                            hero2_magic.append("Blink")
                            print "Here's what spells you have for this hero",hero2_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower() == "yes":
                                print "\n"
                            elif confirm.lower == "no":
                                break
                            break
                    #If user doesn't have a mage
                    elif spell.lower() == "hero2":
                        if hero2.lower() == "black mage" or hero2.lower() == "monk" or hero2.lower() == "warrior":
                            print "This spell doesn't work for that hero, you are getting refunded"
                            balance += 100
                            print "you are still at",balance,"gil"
                                
                    #hero3 equip
                    elif spell == "hero3":
                        if hero3.lower() == "red mage" or hero3.lower() == "white mage":
                            print hero3_name,"learned blink"
                            hero3_magic.append("Blink")
                            print "Here's what spells you have for this hero",hero3_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower()== "yes":
                                print "\n"
                            elif confirm.lower() == "no":
                                break
                    
                    #If user doesn't have a mage
                    elif spell.lower() == "hero3":
                        if hero3.lower() == "black mage" or hero2.lower() == "monk" or hero2.lower() == "warrior":
                            print "This spell doesn't work for that hero, you are getting refunded"
                            balance += 100
                            print "you are still at",balance,"gil"
                    
                    #hero4 equip
                    elif spell.lower() == "hero4":
                        if hero4.lower() == "red mage" or hero4.lower() == "white mage":
                            print hero4_name,"learned protect"
                            hero4_magic.append("Protect")
                            print "Here's what spells you have for this hero",hero4_magic
                            #Asking if user wants to pay for something else
                            confirm = ""
                            confirm = raw_input("Would you like to buy anything else from this category?")
                            if confirm.lower() == "yes":
                                print "\n"
                            elif confirm.lower() == "no":
                                break
                    #If user doesn't have a mage
                    elif spell.lower() == "hero4":
                        if hero4.lower() == "black mage" or hero2.lower() == "monk" or hero2.lower() == "warrior":
                            print "This spell doesn't work for that hero, you are getting refunded"
                            balance += 100
                            print "you are still at",balance,"gil"
                
            #If user has less than the amount of gil needed
            elif confirm.lower() == "yes":
                if balance < blink:
                    print "You don't have enough gil for any magic spells"
                    
            #If user doesn't want spell            
            elif confirm.lower() == "no":
                print "What would you like to buy" 
 
    #Item shop
    while movement.lower() == "item shop":
        print 'The item shop sells a potion and phoenix down'
        item = raw_input("What would you like to buy?<type exit to leave>")
    
        #Potion
        if item.lower() == "potion":
            if balance > potion:
                balance -= 60
                print "Your purchase was successful you are now at",balance,"gil"
                inventory.append("Potion")
                total += 60
            #making a limit on how much the user can fit in  their inventory
            if len(inventory) == 8:
                print "You cannot fit anymore in your inventory"
            #If user doesn't have enough gil
            elif balance < potion:
                print "You do not have enough for this item"
    
        #Phoenix down
        elif item.lower() == "phoenix down":
            #making a limit on how much the user can fit in  their inventory
            if len(inventory) == 8:
                print "You cannot fit anymore in your inventory"
            #If user has enough gil
            if balance > phoenix_down:
                balance -=250
                print "Your purchase was successful, you are now at",balance,"gil"
                inventory.append("Phoenix down")
                total += 250
        #If user doesn't have enough gil
            elif  balance < phoenix_down:
                print "You do not have enough for this item"
    
    #Leaving the town
    
    while movement.lower() == "leave":
        print "You are leaving the town of Cornelia"
        winsound.PlaySound(None, winsound.SND_ASYNC)
        winsound.PlaySound('C:\Users\marco\eclipse-workspace\Grade 10 computer science\Culminating assignemnt\fight.wav', winsound.SND_ASYNC)
        #If user died while fighting       
        if health_for_hero1 == 0 and health_for_hero2 == 0 and health_for_hero3 == 0 and health_for_hero4 == 0:
            break
        
        #Goblin enemy was going to use random to make a differnt amount of enemies spawn but due to time contraints I didn't add but I will try to do it in the future
        enemy_spawned = 3
        
        while enemy_spawned == 3:
            option = raw_input("You came across 3 goblins. What would you like to do (Hint, you can run or attack. However, running will bring you back to town)")
            #Putting in health and damage for first wave of enemy 
            goblin1_health = goblin2_health = goblin3_health = 40
            goblin1_damage = goblin2_damage = goblin3_damage = 12
            #Making user decide on how to attack
            
            if option.lower() == "run":
                run = random.randint(1,3)
                if run == 1 or run == 2:
                    print "You couldn't run, you could try again or attack"
                elif run == 3:
                    print "You were able to run but you will encounter this enemy again"
                    break
            if option.lower() == "attack":
                
                while health_for_hero1 != 0 and health_for_hero2 != 0 and health_for_hero3 != 0 or goblin1_health != 0 and goblin2_health != 0 and goblin3_health != 0:
            
                
                    
                    print "What do you want your first hero",hero1,"to do? (You can attack, use magic, or a item)"
                    hero1_damage = raw_input("What would you like to do? (type attack, magic or item)")
                    if hero1_damage.lower() == "attack":
                        #Choosing which enemy user wants to attack with their first hero
                        enemy = input("Who do you want to attack (type 1 for enemy 1, type 2 for enemy and so on for the amount of enemies you are fighting)")

                        if enemy == 1:
                            if hero1_attack > goblin1_health:
                                damage = hero1_attack - goblin1_health 
                        elif hero1_attack < goblin1_health:
                            damage = goblin1_health = goblin1_health - hero1_attack
                            if goblin1_health >= 0:
                                print "you did",damage,"to the goblin, you defeated a enemy"
                            elif goblin1_health < 0:
                                print "You did",damage,"to the enemy but didn't defeat them "
                    elif enemy == 2:
                        if hero1_attack > goblin2_health:
                                damage = hero1_attack - goblin2_health 
                        elif hero1_attack < goblin2_health:
                            damage = goblin2_health = goblin2_health - hero1_attack
                        if goblin2_health >= 0:
                            print "you did",damage,"to the goblin, you defeated a enemy"
                        elif goblin2_health < 0:
                            print "You did",damage,"to the enemy but didn't defeat them"
                    
                    elif enemy == 3:
                        if hero1_attack > goblin3_health:
                                damage = hero1_attack - goblin3_health 
                        elif hero1_attack < goblin3_health:
                            damage = goblin3_health = goblin3_health - hero1_attack
                        if goblin3_health >= 0:
                            print "you did",damage,"to the goblin, you defeated a enemy"
                        elif goblin3_health < 0:
                            print "You did",damage,"to the enemy but didn't defeat them"
                
                    #Hero1 white magic attacks
                    if hero1_damage.lower() == "white magic":
                        if hero1.lower() == "monk" or hero1.lower() == "warrior" or hero1.lower() == "black magic":
                            print hero1_name,"cannot use white magic spells"
                    #If user has mages that can use white magic
                        elif hero1.lower() == "white mage" or hero1.lower() == "red mage":
                            print "Here's what spells you have for this hero",hero1_magic
                            hero1_magic_attack = raw_input("PLease type in one of the spells you have(note if you are using a red mage, you may see black magic spells")
                        
                            if hero1_magic_attack.lower() != "cure" or hero1_magic_attack.lower() != "dia" or hero1_magic_attack.lower() != "protect" or hero1_magic_attack.lower() != "blink":
                                print "This spell is not a white magic spell"
                        
                            #Using cure on hero1
                            if hero1_magic_attack.lower() == "cure":
                                heal_hero = raw_input("Who do you want to heal?(type hero1, hero2, etc")
                            
                            #Using cure on hero1
                            elif hero1_magic_attack.lower() == "cure":
                                heal_hero = raw_input("Who do you want to heal?(type hero1, hero2, etc")
                                #Using cure on hero1
                                if heal_hero.lower() == "hero1":
                                    if health_for_hero1 == health_for_hero1_with_armor:
                                        print "You cannot heal this hero as there health is max"
                                elif health_for_hero1 < health_for_hero1_with_armor:
                                    print hero1_name,"used cure to heal itself by 15 hp"
                                    health_for_hero1 += 15
                                    #If cure restores more than max health
                                    if health_for_hero1 > health_for_hero1_with_armor:
                                        health_for_hero1 = 50
                                #Using cure to heal hero2
                                elif heal_hero.lower() == "hero2":
                                    if health_for_hero2 == health_for_hero2_with_armor:
                                        print "You cannot heal",hero2_name
                                #If hero has less health
                                elif health_for_hero2 < health_for_hero2_with_armor:
                                    print hero1_name,"used cure to heal",hero2_name,"by 15 hp"
                                    health_for_hero2 +=15
                                    #If cure restores more than max health
                                    if health_for_hero2 > health_for_hero2_with_armor:
                                        health_for_hero2 = 50
                                #Using cure to heal hero3
                                elif heal_hero.lower() == "hero3":
                                    if health_for_hero3 == health_for_hero3_with_armor:
                                        print "You cannot heal",hero3_name
                                elif health_for_hero3 < health_for_hero3_with_armor: 
                                    print hero1_name,"used cure to heal",hero3_name,"by 15 hp"
                                    health_for_hero3 +=15
                                    #If cure restores more than max health
                                    if health_for_hero3 > health_for_hero3_with_armor:
                                        health_for_hero3 = 50 
                                #Using cure to heal hero4
                                elif heal_hero.lower() == "hero4":
                                    if health_for_hero4 == health_for_hero4_with_armor:
                                        print "You cannot heal",hero4_name
                                elif health_for_hero4 < health_for_hero4_with_armor:
                                    print hero1_name,"used cure to heal",hero4_name,"by 15 hp"
                                    health_for_hero4 +=15
                                    #If cure restores more than max health
                                    if health_for_hero4 > health_for_hero4_with_armor:
                                        health_for_hero4 = 50
                        
                            #If user wants to use dia
                            elif hero1_magic_attack.lower() == "dia":
                                dia_attack = input("Which enemy do you want to attack out of the 3. You can type 1, 2 or 3")
                                #Using dia on the first goblin
                                if dia_attack == 1:
                                    print hero1,"attacked goblin 1 for 20 damage"
                                #Lowering enemy's health
                                    goblin1_health -= 20
                                    if goblin1_health < 0:
                                        print hero1_name,"did defeat goblin 1"
                                    elif goblin1_health > 0:
                                        print hero1_name,"did not defeat goblin 1"
                                #Using dia on second goblin
                                elif dia_attack == 2:
                                    print hero1,"attacked goblin 2 for 20 damage"
                                #Lowering enemy's health
                                    goblin2_health -= 20
                                    if goblin2_health < 0:
                                        print hero1_name,"did defeat goblin 2"
                                    elif goblin2_health > 0:
                                        print hero1_name,"did not defeat goblin 2"
                                #Using dia on the third goblin
                                elif dia_attack == 3:
                                    print hero1,"attacked goblin 3 for 20 damage"
                                #Lowering enemy's health
                                    goblin3_health -= 20
                                    if goblin3_health < 0:
                                        print hero1_name,"did defeat goblin 1"
                                    elif goblin3_health > 0:
                                        print hero1_name,"did not defeat goblin 1"
                                
                            #If user wants to use protect
                            elif hero1_magic_attack.lower() == "protect":
                                protect_attack = raw_input("Which hero do you want to use this on, you can type hero1, hero2, hero3, or hero4")
                                #Using protect on first hero
                                if protect_attack.lower() == "hero1":
                                    print hero1,"used protect to increase their health by 8 points. This spell lasts forever, until the hero's health decreases"
                                    health_for_hero1 += 8
                                #Using protect on second hero
                                elif protect_attack.lower() == "hero2":
                                    print hero1,"used protect to increase",hero2_name,"health by 8 points. This spell lasts forever, until the hero's health decreases"
                                    health_for_hero2 += 8
                                #Using protect on third hero
                                elif protect_attack.lower() == "hero3":
                                    print hero1,"used protect to increase their health by 8 points. This spell lasts forever, until the hero's health decreases"
                                    health_for_hero3 += 8
                                #Using protect on fourth hero
                                elif protect_attack.lower() == "hero4":
                                    print hero1,"used protect to increase",hero4_name,"health by 8 points. This spell lasts forever, unti the hero's health decreases"
                                    health_for_hero4 += 8
                        
                            #If user wants to use blink
                            elif hero1_magic_attack.lower() == "blink":
                                print hero1_name,"used blink to increase the chance of not getting attacked by enemies"
                
                    #Hero1 black magic attacks
                    elif hero1_damage.lower() == "black magic":
                        if hero1.lower() == "monk" or hero1.lower() == "warrior" or hero1.lower() == "white mage": 
                            print hero1_name,"cannot use black magic spells"
                        #If user has mages that can use white magic
                        elif hero1.lower() == "black mage" or hero1.lower() == "red mage":
                            print "Here's what spells you have for this hero",hero1_magic
                            hero1_magic_attack = raw_input("PLease type in one of the spells you have")
                        
                        if hero1_magic_attack.lower() != "fire" or hero1_magic_attack.lower() != "sleep" or hero1_magic_attack.lower() != "thunder":
                            print "This spell is not a white magic spell"
                        
                            #Using fire for hero1
                            if hero1_magic_attack.lower() == "fire":
                                fire_attack = input("Which enemy do want to use this spell on, you can type 1, 2, 3 or 4")
                                #Using fire attack on goblin 1
                                if fire_attack == 1:
                                    goblin1_health -=10
                                    print hero1_name,"attacked goblin 1 for 10 damage"
                                    if goblin1_health <= 0:
                                        print hero1_name,"defeated goblin 1"
                                    elif goblin1_health > 0:
                                        print hero1_name,"did not deal enough damage to defeat goblin1"  
                                #using fire attack on goblin 2
                                elif fire_attack == 2:
                                    goblin2_health -=10
                                    print hero2_name,"attacked goblin 2 for 10 damage"
                                    if goblin2_health <= 0:
                                        print hero1_name,"defeated goblin 2"
                                    elif goblin2_health > 0:
                                        print hero1_name,"did not deal enough damage to defeat goblin1" 
                                #Using fire attack on goblin 3
                                elif fire_attack == 3:
                                    goblin3_health -=10
                                    print hero1_name,"attacked goblin 1 for 10 damage"
                                    if goblin3_health <= 0:
                                        print hero1_name,"defeated goblin 3"
                                    elif goblin3_health > 0:
                                        print hero1_name,"did not deal enough damage to defeat goblin1" 
                        
                                #using sleep for hero1
                                elif hero1_magic_attack.lower() == "sleep":
                                    sleep_attack = random.randint(1,10)
                                    if sleep_attack == 1 or sleep_attack ==2:
                                        print "All enemies were put to sleep, they will miss their turn"
                                    elif sleep_attack == 3 or sleep_attack == 4 or sleep_attack == 5 or sleep_attack == 6 or sleep_attack == 7 or sleep_attack == 8 or sleep_attack == 9 or sleep_attack == 10:
                                        print "The spell didn't work on the enemies"
                                
                                #Using thunder for hero1
                                elif hero1_magic_attack.lower() == "thunder":
                                    thunder_attack = input("Which enemy would you like to use this spell on, type 1, 2, 3 or 4")
                                #using thunder on goblin 1
                                if thunder_attack == 1:
                                    goblin1_health -=12
                                    print hero1_name,"dealt 12 damage to goblin 1"
                                    if goblin1_health <= 0:
                                        print hero1_name,"defeated goblin 1"
                                    elif goblin1_health > 0:
                                        print hero1_name,"was not able to defeat goblin 1"
                                #Using thunder on goblin 2
                                elif thunder_attack == 1:
                                    goblin2_health -=12
                                    print hero1_name,"dealt 12 damage to goblin 2"
                                    if goblin2_health <= 0:
                                        print hero1_name,"defeated goblin 2"
                                    elif goblin2_health > 0:
                                        print hero1_name,"was not able to defeat goblin 2"
                                #using thunder on goblin 3
                                if thunder_attack == 3:
                                    goblin3_health -=12
                                    print hero1_name,"dealt 12 damage to goblin 1"
                                    if goblin3_health <= 0:
                                        print hero1_name,"defeated goblin 1"
                                    elif goblin3_health > 0:
                                        print hero1_name,"was not able to defeat goblin 1"
                            
                    #Showing inventory
                    if hero1_damage.lower() == "item":
                        print "Here's what items you have",inventory 
                        use_inventory = input("Please type in the number of the item to use(ex if Potion shows first, type 1)")   
                    
                        if use_inventory.lower() == "potion":
                            heal_potion = raw_input("Who do you want to use this potion on(type hero1, hero2, hero3, or hero4")
                            #Using potion on hero1
                            if heal_potion.lower() == "hero1":
                                if health_for_hero1 == health_for_hero1_with_armor:
                                    print "you cannot use a potion on this because it's health is full"
                                elif health_for_hero1 < health_for_hero1_with_armor:
                                    if "Potion" in inventory:
                                        #Removing the item used
                                        inventory.remove('Potion')
                                        print hero1_name,"healed themselves for 15 points"
                                        health_for_hero1 +=15
                                        #If potion heals more health than intended
                                        if health_for_hero1 > health_for_hero1_with_armor:
                                            health_for_hero1 = 50 
                                            print hero1_name,"(",hero1,"), is now at",health_for_hero1,"hp"
                                    else:
                                        if "Potion" in inventory:
                                            #Removing the item used
                                            inventory.remove('Potion')
                                            print hero1_name,"(",hero1,"), is now at",health_for_hero1,"hp"
                            #Using potion on hero2    
                            elif heal_potion.lower() == "hero2":
                                if health_for_hero2 == health_for_hero2_with_armor:
                                    print "you cannot use a potion on this hero because it's health is full"
                                elif health_for_hero2 < health_for_hero2_with_armor:
                                    if "Potion" in inventory:
                                        #Removing the item used
                                        inventory.remove('Potion')
                                        print hero1_name,"healed for 15 points"
                                        health_for_hero2 +=15
                                    #If potion heals more health than intended
                                        if health_for_hero2 > health_for_hero2_with_armor:
                                            health_for_hero2 = 50
                                            print hero2_name,"(",hero2,"), is now at",health_for_hero2,"hp"
                                    else:
                                        if "Potion" in inventory:
                                            #Removing the item used
                                            inventory.remove('Potion')
                                            print hero2_name,"(",hero2,"), is now at",health_for_hero2,"hp"
                            #Using potion on hero3
                            elif heal_potion.lower() == "hero3":
                                if health_for_hero3 == health_for_hero3_with_armor:
                                    print "you cannot use a potion on this because it's health is full"
                                elif health_for_hero3 < health_for_hero3_with_armor:
                                    if "Potion" in inventory:
                                        #Removing the item used
                                        inventory.remove('Potion')
                                        print hero1_name,"healed for 15 points"
                                        health_for_hero3 +=15
                                #If potion heals more health than intended
                                    if health_for_hero3 > health_for_hero3_with_armor:
                                        health_for_hero3 = 50
                                        print hero3_name,"(",hero3,"), is now at",health_for_hero3,"hp"
                                        
                                    #If hero's health isn't less or more than 50
                                    else:
                                        if "Potion" in inventory:
                                            #Removing the item used
                                            inventory.remove('Potion')
                                            print hero3_name,"(",hero3,"), is now at",health_for_hero3,"hp"
                            #Using potion on hero4
                            elif heal_potion.lower() == "hero4":
                                if health_for_hero4 == health_for_hero4_with_armor:
                                    print "you cannot use a potion on this because it's health is full"
                                elif health_for_hero4 < health_for_hero4_with_armor:
                                    if "Potion" in inventory:
                                        #Removing the item used
                                        inventory.remove('Potion')
                                        print hero4_name,"healed for 15 points"
                                        health_for_hero4 +=15
                                        #If potion heals more health than intended
                                        if health_for_hero4 > health_for_hero4_with_armor:
                                            health_for_hero4 = 50
                                            print hero4_name,"(",hero4,"), is now at",health_for_hero4,"hp"
                                    #If hero's health isn't less or more than 50
                                    else:
                                        if "Potion" in inventory:
                                            #Removing the item used
                                            inventory.remove('Potion')
                                            print hero4_name,"(",hero4,"), is now at",health_for_hero4,"hp"
                        #Using phoenix down
                        elif use_inventory.lower() == "phoenix down":
                            use_phoenix_down = raw_input("Who do you want to use this phoenix down on(type hero1, hero2, hero3, or hero4")
                            #Using phoenix down on hero1
                            if use_phoenix_down.lower() == "hero1":
                                print "You cannot use phoenix down on this hero because it is alive"
                                if "Phoenix down" in inventory:
                                    inventory.remove('Phoenix down')
                            #Using phoenix down on hero2
                            elif use_phoenix_down.lower() == "hero2":        
                                    if health_for_hero2 > 0:
                                        print "You cannot use a phoenix down on",hero2_name,"because their health if full"
                                    elif health_for_hero2 <= 0:
                                        health_for_hero2 = 20
                                        print "You used phoenix down on",hero2_name,"their health is now at",health_for_hero2
                                        if "Phoenix down" in inventory:
                                            inventory.remove('Phoenix down')
                            
                                
                            #Using phoenix down on hero3
                            elif use_phoenix_down.lower() == "hero3":        
                                    if health_for_hero3 <= 0:
                                        health_for_hero3 = 20
                                        print hero1_name,"used phoenix down on",hero3_name,". Their health is now",health_for_hero3
                                        if "Phoenix down" in inventory:
                                            inventory.remove('Phoenix down')
                                    #If health is full or character is living
                                    elif health_for_hero3 > 0:
                                        print "You cannot use a phoenix down on",hero3_name,"because they are at full health"
                            #Using phoenix down on hero4
                            elif use_phoenix_down.lower() == "hero4":        
                                    if health_for_hero4 == 0:
                                        health_for_hero4 = 20
                                        if "Phoenix down" in inventory:
                                            inventory.remove('Phoenix down')
                                            print hero1_name,"used phoenix down on",hero4_name,". Their health is now",health_for_hero4
                                    #If health is full or character is living
                                    elif health_for_hero4 > 0:
                                        print "You cannot use a phoenix down on",hero4_name,"because they are at full health"
                        
                    #Hero2 attack
                    print "What do you want your second hero",hero2,"to do? (You can attack, use a spell, or a item)"
                    hero2_damage = raw_input("What would you like to do? (Type attack, magic or item")
                    if hero2_damage.lower() == "attack":
                        #Choosing which enemy user wants to attack with their second hero
                        enemy = input("Who do you want to attack (type 1 for enemy 1, type 2 for enemy and so on for the amount of enemies you are fighting)")
                        if enemy == 1:
                            if hero2_attack > goblin1_health:
                                damage = goblin1_health = hero2_attack - goblin1_health 
                            elif hero2_attack < goblin1_health:
                                damage =  goblin1_health =  goblin1_health - hero2_attack 
                        
                            if goblin1_health < 0:
                                print hero2_name,"did defeat goblin 1"
                            elif goblin1_health > 0:
                                print hero2_name,"did not defeat goblin 1"
                            elif goblin1_health == 0:
                                print "You cannot attack this enemy because it is dead "
                            
                        
                    elif enemy == 2:
                        if hero2_attack > goblin2_health:
                                damage = hero2_attack - goblin2_health 
                        elif hero2_attack < goblin2_health:
                            damage = goblin2_health = goblin2_health - hero2_attack
                        
                        if goblin2_health >= 0:
                            print "you did",damage,"to the goblin, you defeated a enemy"
                        elif goblin2_health < 0:
                            print "You did",damage,"to the enemy but didn't defeat them"
                        elif goblin2_health == 0:
                            print "You cannot attack this enemy because it is dead"
                    
                    elif enemy == 3:
                        if hero2_attack > goblin3_health:
                                damage = hero2_attack - goblin3_health 
                        elif hero2_attack < goblin3_health:
                            damage =  goblin3_health = goblin3_health - hero2_attack
                        if damage >= goblin3_health:
                            print "you did",damage,"to the goblin, you defeated a enemy"
                        elif damage < goblin3_health:
                            print "You did",damage,"to the enemy but didn't defeat them"
                        elif goblin3_health == 0:
                            print "You cannot attack this enemy because they are dead"
                        
                    #Hero2 white magic attacks
                    elif hero2_damage.lower() == "white magic":
                        if hero2.lower() == "monk" or hero2.lower() == "warrior" or hero2.lower() == "black mage":
                            print hero2_name,"cannot use white magic"
                        elif hero2.lower() == "white mage" or hero2.lower() == "red mage":
                            print "Here's what spells you have for this hero",hero2_magic
                            hero2_magic_attack = raw_input("PLease type in one of the spells you have(note if you are using a red mage you may see your black magic spells but you cannot use these)")
                        
                            if hero2_magic_attack.lower() != "cure" or hero2_magic_attack.lower() != "dia" or hero2_magic_attack.lower() != "protect" or hero2_magic_attack.lower() != "blink":
                                print "This spell is not a white magic spell"
                                #defining heal hero because python wont accept it
                            heal_hero = ""
                        
                            #Using cure on hero1
                            if hero2_magic_attack.lower() == "cure":
                                heal_hero = raw_input("Who do you want to heal?(type hero1, hero2, etc")
                                #Using cure on hero1
                                if heal_hero.lower() == "hero1":
                                    if health_for_hero1 == health_for_hero1_with_armor:
                                        print "You cannot heal this hero as there health is max"
                                elif health_for_hero1 < health_for_hero1_with_armor:
                                    print hero2_name,"used cure to heal",hero1_name,"by 15 hp"
                                    health_for_hero1 += 15
                                    #If cure restores more than max health
                                    if health_for_hero1 > health_for_hero1_with_armor:
                                        health_for_hero1 = 50
                                #Using cure to heal hero2
                                elif heal_hero.lower() == "hero2":
                                    if health_for_hero2 == health_for_hero2_with_armor:
                                        print "You cannot heal",hero2_name
                                    #If hero has less health
                                elif health_for_hero2 < health_for_hero2_with_armor:
                                    print hero2_name,"used cure to heal itself by 15 hp"
                                    health_for_hero2 +=15
                                    #If cure restores more than max health
                                    if health_for_hero2 > health_for_hero2_with_armor:
                                        health_for_hero2 = 50
                                #Using cure to heal hero3
                                elif heal_hero.lower() == "hero3":
                                    if health_for_hero3 == health_for_hero3_with_armor:
                                        print "You cannot heal",hero3_name
                                elif health_for_hero3 < health_for_hero3_with_armor: 
                                    print hero2_name,"used cure to heal",hero3_name,"by 15 hp"
                                    health_for_hero3 +=15
                                    #If cure restores more than max health
                                    if health_for_hero3 > health_for_hero3_with_armor:
                                        health_for_hero3 = 50 
                                    #Using cure to heal hero4
                                    elif heal_hero.lower() == "hero4":
                                        if health_for_hero4 == health_for_hero4_with_armor:
                                            print "You cannot heal",hero4_name
                                elif health_for_hero4 < health_for_hero4_with_armor:
                                    print hero2_name,"used cure to heal",hero4_name,"by 15 hp"
                                    health_for_hero4 +=15
                                #If cure restores more than max health
                                    if health_for_hero4 > health_for_hero4_with_armor:
                                        health_for_hero4 = 50
                        
                            #If user wants to use dia
                            elif hero2_magic_attack.lower() == "dia":
                                dia_attack = input("Which enemy do you want to attack out of the 3. You can type 1, 2 or 3")
                                #Using dia on the first goblin
                                if dia_attack == 1:
                                    print hero2,"attacked goblin 1 for 20 damage"
                                    #Lowering enemy's health
                                    goblin1_health -= 20
                                #Using dia on second goblin
                                elif dia_attack == 2:
                                    print hero2,"attacked goblin 2 for 20 damage"
                                    #Lowering enemy's health
                                    goblin2_health -= 20
                                #Using dia on the third goblin
                                elif dia_attack == 3:
                                    print hero2,"attacked goblin 3 for 20 damage"
                                    #Lowering enemy's health
                                    goblin3_health -= 20
                                
                            #If user wants to use protect
                            elif hero2_magic_attack.lower() == "protect":
                                protect_attack = raw_input("Which hero do you want to use this on, you can type hero1, hero2, hero3, or hero4")
                                #Using protect on first hero
                                if protect_attack.lower() == "hero1":
                                    print hero2_name,"used protect to increase",hero1_name,"health by 8 points. This spell lasts forever until the heros health decreases"
                                    health_for_hero1 += 8
                                #Using protect on second hero
                                elif protect_attack.lower() == "hero2":
                                    print hero2_name,"used protect to increase it's health by 8 points. This spell lasts forever until the heros health decreases"
                                    health_for_hero2 += 8
                                #Using protect on third hero
                                elif protect_attack.lower() == "hero3":
                                    print hero2_name,"used protect to increase,",hero3_name,"This spell lasts forever until the heros health decreases"
                                    health_for_hero3 += 8
                                #Using protect on fourth hero
                                elif protect_attack.lower() == "hero4":
                                    print hero2_name,"used protect to increase",hero4_name,"health by 8 points. This spell lasts forever until the heros health decreases"
                                    health_for_hero4 += 8
                        
                            #If user wants to use blink
                            elif hero2_magic_attack.lower() == "blink":
                                print hero2_name,"used blink to increase the chance of not getting attacked by enemies"
                        
                #Hero2 black magic attacks
                    elif hero2_damage.lower() == "black magic":
                        if hero2.lower() == "monk" or hero2.lower() == "warrior" or hero2.lower() == "white mage": 
                            print hero2_name,"cannot use black magic spells"
                        #If user has mages that can use white magic
                        elif hero2.lower() == "black mage" or hero2.lower() == "red mage":
                            print "Here's what spells you have for this hero",hero2_magic
                            hero2_magic_attack = raw_input("PLease type in one of the spells you have")
                        
                            if hero2_magic_attack.lower() != "fire" or hero2_magic_attack.lower() != "sleep" or hero2_magic_attack.lower() != "thunder":
                                print "This spell is not a white magic spell"
                        
                            #Using fire for hero1
                            elif hero2_magic_attack.lower() == "fire":
                                fire_attack = input("Which enemy do want to use this spell on, you can type 1, 2, 3 or 4")
                                #Using fire attack on goblin 1
                                if fire_attack == 1:
                                    goblin1_health -=10
                                    print hero2_name,"attacked goblin 1 for 10 damage"
                                    if goblin1_health <= 0:
                                        print hero2_name,"defeated goblin 1"
                                    elif goblin1_health > 0:
                                        print hero2_name,"did not deal enough damage to defeat goblin1"  
                                #using fire attack on goblin 2
                                elif fire_attack == 2:
                                    goblin2_health -=10
                                    print hero2_name,"attacked goblin 2 for 10 damage"
                                    if goblin2_health <= 0:
                                        print hero2_name,"defeated goblin 2"
                                    elif goblin2_health > 0:
                                        print hero2_name,"did not deal enough damage to defeat goblin1" 
                                #Using fire attack on goblin 3
                                elif fire_attack == 3:
                                    goblin1_health -=10
                                    print hero2_name,"attacked goblin 1 for 10 damage"
                                    if goblin1_health <= 0:
                                        print hero2_name,"defeated goblin 3"
                                    elif goblin1_health > 0:
                                        print hero2_name,"did not deal enough damage to defeat goblin1" 
                        
                            #using sleep for hero2
                            elif hero2_magic_attack.lower() == "sleep":
                                sleep_attack = random.randint(1,10)
                                if sleep_attack == 1 or sleep_attack == 2:
                                    print "All enemies were put to sleep, they will miss their turn"
                                elif sleep_attack == 3 or sleep_attack == 4 or sleep_attack == 5 or sleep_attack == 6 or sleep_attack == 7 or sleep_attack == 8 or sleep_attack == 9 or sleep_attack == 10:
                                    print "The spell didn't work on the enemies"
                        
                        
                                
                            #Using thunder for hero2
                            elif hero2_magic_attack.lower() == "thunder":
                                thunder_attack = input("Which enemy would you like to use this spell on, type 1, 2, 3 or 4")
                                #using thunder on goblin 1
                                if thunder_attack == 1:
                                    goblin1_health -=12
                                    print hero2_name,"dealt 12 damage to goblin 1"
                                    if goblin1_health <= 0:
                                        print hero2_name,"defeated goblin 1"
                                    elif goblin1_health > 0:
                                        print hero2_name,"was not able to defeat goblin 1"
                                #Using thunder on goblin 2
                                elif thunder_attack == 1:
                                    goblin2_health -=12
                                    print hero2_name,"dealt 12 damage to goblin 2"
                                    if goblin2_health <= 0:
                                        print hero2_name,"defeated goblin 2"
                                    elif goblin2_health > 0:
                                        print hero2_name,"was not able to defeat goblin 2"
                                #using thunder on goblin 3
                                if thunder_attack == 3:
                                    goblin3_health -=12
                                    print hero2_name,"dealt 12 damage to goblin 1"
                                    if goblin3_health <= 0:
                                        print hero2_name,"defeated goblin 1"
                                    elif goblin3_health > 0:
                                        print hero2_name,"was not able to defeat goblin 1"
                
                    #Showing inventory
                    elif hero2_damage.lower() == "item":
                        print "Here's what items you have",inventory
                        use.inventory = raw_input("What item do you want to use?")
                    
                        if use_inventory.lower() == "potion":
                            heal_potion = raw_input("Who do you want to use this potion on(type hero1, hero2, hero3, or hero4")
                            #Using potion on hero1
                            if heal_potion.lower() == "hero1":
                                if health_for_hero1 == health_for_hero1_with_armor:
                                    print "you cannot use a potion on this because it's health is full"
                                elif health_for_hero1 < health_for_hero1_with_armor:
                                    if "Potion" in inventory:
                                        #Removing the item used
                                        inventory.remove('Potion')
                                        print hero1_name,"healed themselves for 15 points"
                                        health_for_hero1 +=15
                                        #If potion heals more health than intended
                                        if health_for_hero1 > health_for_hero1_with_armor:
                                            health_for_hero1 = 50 
                                            print hero1_name,"(",hero1,"), is now at",health_for_hero1,"hp"
                                    else:
                                        if "Potion" in inventory:
                                            #Removing the item used
                                            inventory.remove('Potion')
                                            print hero1_name,"(",hero1,"), is now at",health_for_hero1,"hp"
                            #Using potion on hero2    
                            elif heal_potion.lower() == "hero2":
                                if health_for_hero2 == health_for_hero2_with_armor:
                                    print "you cannot use a potion on this hero because it's health is full"
                                elif health_for_hero2 < health_for_hero2_with_armor:
                                    if "Potion" in inventory:
                                        #Removing the item used
                                        inventory.remove('Potion')
                                        print hero1_name,"healed for 15 points"
                                        health_for_hero2 +=15
                                    #If potion heals more health than intended
                                        if health_for_hero2 > health_for_hero2_with_armor:
                                            health_for_hero2 = 50
                                            print hero2_name,"(",hero2,"), is now at",health_for_hero2,"hp"
                                    else:
                                        if "Potion" in inventory:
                                            #Removing the item used
                                            inventory.remove('Potion')
                                            print hero2_name,"(",hero2,"), is now at",health_for_hero2,"hp"
                            #Using potion on hero3
                            elif heal_potion.lower() == "hero3":
                                if health_for_hero3 == health_for_hero3_with_armor:
                                    print "you cannot use a potion on this because it's health is full"
                                elif health_for_hero3 < health_for_hero3_with_armor:
                                    if "Potion" in inventory:
                                        #Removing the item used
                                        inventory.remove('Potion')
                                        print hero1_name,"healed for 15 points"
                                        health_for_hero3 +=15
                                        #If potion heals more health than intended
                                        if health_for_hero3 > health_for_hero3_with_armor:
                                            health_for_hero3 = 50
                                            print hero3_name,"(",hero3,"), is now at",health_for_hero3,"hp"
                                        #If hero's health isn't less or more than 50
                                    else:
                                        if "Potion" in inventory:
                                            #Removing the item used
                                            inventory.remove('Potion')
                                            print hero3_name,"(",hero3,"), is now at",health_for_hero3,"hp"
                            #Using potion on hero4
                            elif heal_potion.lower() == "hero4":
                                if health_for_hero4 == health_for_hero4_with_armor:
                                    print "you cannot use a potion on this because it's health is full"
                                elif health_for_hero4 < health_for_hero4_with_armor:
                                    if "Potion" in inventory:
                                        #Removing the item used
                                        inventory.remove('Potion')
                                        print hero4_name,"healed for 15 points"
                                        health_for_hero4 +=15
                                        #If potion heals more health than intended
                                        if health_for_hero4 > health_for_hero4_with_armor:
                                            health_for_hero4 = 50
                                            print hero4_name,"(",hero4,"), is now at",health_for_hero4,"hp"
                                    #If hero's health isn't less or more than 50
                                    else:
                                        if "Potion" in inventory:
                                            #Removing the item used
                                            inventory.remove('Potion')
                                            print hero4_name,"(",hero4,"), is now at",health_for_hero4,"hp"
                            #Using phoenix down
                            elif use_inventory.lower() == "phoenix down":
                                use_phoenix_down = raw_input("Who do you want to use this phoenix down on(type hero1, hero2, hero3, or hero4")
                                #Using phoenix down on hero1
                                if use_phoenix_down.lower() == "hero1":
                                    if health_for_hero1 > 0 :
                                        print "You cannot use a phoenix down on",hero1_name,"because their health if full"
                                elif health_for_hero1 <= 0 :
                                    health_for_hero1 = 20
                                    print "You used phoenix down on",hero1_name,"their health is now at",health_for_hero1
                                    if "Phoenix down" in inventory:
                                        inventory.remove('Phoenix down')
                            #Using phoenix down on hero2
                            elif use_phoenix_down.lower() == "hero2":        
                                print "You cannot use a phoenix down on",hero2_name,"because their health if full"
                                
                            #Using phoenix down on hero3
                            elif use_phoenix_down.lower() == "hero3":        
                                if health_for_hero3 <= 0:
                                    health_for_hero3 = 20
                                    print hero2_name,"used phoenix down on",hero3_name,". Their health is now",health_for_hero3
                                    if "Phoenix down" in inventory:
                                        inventory.remove('Phoenix down')
                                #If health is full or character is living
                                elif health_for_hero3 > 0:
                                    print "You cannot use a phoenix down on",hero3_name,"because they are at full health"
                            #Using phoenix down on hero4
                            elif use_phoenix_down.lower() == "hero4":        
                                if health_for_hero4 == 0:
                                    health_for_hero4 = 20
                                    if "Phoenix down" in inventory:
                                        inventory.remove('Phoenix down')
                                        print hero2_name,"used phoenix down on",hero4_name,". Their health is now",health_for_hero4
                                #If health is full or character is living
                                elif health_for_hero4 > 0:
                                    print "You cannot use a phoenix down on",hero4_name,"because they are at full health"
                #Hero3 attack
                    print "What do you want your third hero",hero3,"to do? (You can attack, use a spell, or a item)"
                    hero3_damage = raw_input("What would you like to do? (Type attack, white magic, black magic,  or item")
                    if hero3_damage.lower() == "attack":
                        #Choosing which enemy user wants to attack with their second hero
                        enemy = input("Who do you want to attack (type 1 for enemy 1, type 2 for enemy and so on for the amount of enemies you are fighting)")
                        if enemy == 1:
                            if hero3_attack > goblin1_health:
                                damage = hero3_attack - goblin1_health 
                            elif hero3_attack < goblin1_health:
                                damage = goblin1_health =  goblin1_health - hero3_attack 
                            if goblin1_health >= 0:
                                print "you did",damage,"to the goblin, you defeated a enemy"
                            elif goblin1_health < 0:
                                print "You did",damage,"to the enemy but didn't defeat them "
                    
                        elif enemy == 2:
                            if hero3_attack > goblin2_health:
                                damage = hero3_attack - goblin2_health 
                            elif hero3_attack < goblin3_health:
                                damage = goblin2_health= goblin2_health - hero3_attack 
                            
                            if goblin2_health >= 0:
                                print "you did",damage,"to the goblin, you defeated a enemy"
                            elif goblin2_health < 0:
                                print "You did",damage,"to the enemy but didn't defeat them"
                    
                        elif enemy == 3:
                            if hero3_attack > goblin3_health:
                                damage = hero3_attack - goblin3_health 
                            elif hero3_attack < goblin3_health:
                                damage = goblin3_health = goblin3_health - hero3_attack 
                            
                            if goblin3_health >= 0:
                                print "you did",damage,"to the goblin, you defeated a enemy"
                            elif goblin3_health< 0:
                                print "You did",hero_damage,"to the enemy but didn't defeat them"
                        
                    #Hero3 white magic attacks
                    elif hero3_damage.lower() == "white magic":
                        #If user has characters that cannot use white magic
                        if hero3.lower() == "monk" or hero3.lower() == "warrior" or hero3.lower() == "black mage":
                            print hero3,"cannot use white magic"
                        #If user has characters that can use white magic
                        elif hero3.lower() == "white mage" or hero3.lower() == "red mage":
                            print "Here's what spells you have for this hero",hero3_magic
                            hero3_magic_attack = raw_input("PLease type in one of the spells you have(note, if you have a red mage mage, your black magic spells may show up but you must use white magic spells)")
                        
                            if hero3_magic_attack.lower() != "cure" or hero3_magic_attack.lower() != "dia" or hero3_magic_attack.lower() != "protect" or hero3_magic_attack.lower() != "blink":
                                print "This spell is not a white magic spell"
                            #Using cure on hero1
                            elif hero3_magic_attack.lower() == "cure":
                                heal_hero = raw_input("Who do you want to heal?(type hero1, hero2, etc")
                                #Using cure on hero1
                                if heal_hero.lower() == "hero1":
                                    if health_for_hero1 == health_for_hero1_with_armor:
                                        print "You cannot heal this hero as there health is max"
                                elif health_for_hero1 < health_for_hero1_with_armor:
                                    print hero3_name,"used cure to heal,",hero1_name,"by 15 hp"
                                    health_for_hero1 += 15
                                    #If cure restores more than max health
                                    if health_for_hero1 > health_for_hero1_with_armor:
                                        health_for_hero1 = 50
                                #Using cure to heal hero2
                                elif heal_hero.lower() == "hero2":
                                    if health_for_hero2 == health_for_hero2_with_armor:
                                        print "You cannot heal",hero2_name
                                    #If hero has less health
                                    elif health_for_hero2 < health_for_hero2_with_armor:
                                        print hero3_name,"used cure to heal",hero2_name,"by 15 hp"
                                        health_for_hero2 +=15
                                    #If cure restores more than max health
                                    if health_for_hero2 > health_for_hero2_with_armor:
                                        health_for_hero2 = 50
                                #Using cure to heal hero3
                                elif heal_hero.lower() == "hero3":
                                    if health_for_hero3 == health_for_hero3_with_armor:
                                        print "You cannot heal",hero3_name
                                elif health_for_hero3 < health_for_hero3_with_armor: 
                                    print hero3_name,"used cure to heal",hero2_name,"by 15 hp"
                                    health_for_hero3 +=15
                                    #If cure restores more than max health
                                    if health_for_hero3 > health_for_hero3_with_armor:
                                        health_for_hero3 = 50 
                                    #Using cure to heal hero4
                                elif heal_hero.lower() == "hero4":
                                    if health_for_hero4 == health_for_hero4_with_armor:
                                        print "You cannot heal",hero4_name
                                elif health_for_hero4 < health_for_hero4_with_armor:
                                    print hero4_name,"used cure to heal themselve by 15 hp"
                                    health_for_hero4 +=15
                                #If cure restores more than max health
                                    if health_for_hero4 > health_for_hero4_with_armor:
                                        health_for_hero4 = 50
                        
                            #If user wants to use dia
                            elif hero3_magic_attack.lower() == "dia":
                                dia_attack = input("Which enemy do you want to attack out of the 3. You can type 1, 2 or 3")
                                #Using dia on the first goblin
                                if dia_attack == 1:
                                    print hero3,"attacked goblin 1 for 20 damage"
                                    #Lowering enemy's health
                                    goblin1_health -= 20
                                #Using dia on second goblin
                                elif dia_attack == 2:
                                    print hero3,"attacked goblin 2 for 20 damage"
                                    #Lowering enemy's health
                                    goblin2_health -= 20
                                #Using dia on the third goblin
                                elif dia_attack == 3:
                                    print hero3,"attacked goblin 2 for 20 damage"
                                    #Lowering enemy's health
                                    goblin3_health -= 20
                                
                            #If user wants to use protect
                            elif hero3_magic_attack.lower() == "protect":
                                protect_attack = raw_input("Which hero do you want to use this on, you can type hero1, hero2, hero3, or hero4")
                                #Using protect on first hero
                                if protect_attack.lower() == "hero1":
                                    print hero3,"used protect to increase",hero1_name,"health by 8 points. This spell lasts forever, until the hero's health decreases"
                                    health_for_hero1 += 8
                                #Using protect on second hero
                                elif protect_attack.lower() == "hero2":
                                    print hero3,"used protect to increase",hero2_name,"health by 8 points. This spell lasts forever, until the hero's health decreases"
                                    health_for_hero2 += 8
                                #Using protect on third hero
                                elif protect_attack.lower() == "hero3":
                                    print hero3,"used protect to increase their health by 8 points. This spell lasts forever, until the hero's health decreases"
                                    health_for_hero3 += 8
                                #Using protect on fourth hero
                                elif protect_attack.lower() == "hero4":
                                    print hero3,"used protect to increase",hero4_name,"health by 8 points. This spell lasts forever, until the hero's health decreases"
                                    health_for_hero4 += 8
                
                            #If user wants to use blink
                            elif hero3_magic_attack.lower() == "blink":
                                print hero3_name,"used blink to increase the chance of not getting attacked by enemies"
                        
                            #Hero3 black magic attacks
                            elif hero3_damage.lower() == "black magic":
                                if hero3.lower() == "monk" or hero3.lower() == "warrior" or hero3.lower() == "white mage": 
                                    print hero3_name,"cannot use black magic spells"
                            #If user has mages that can use white magic
                            elif hero3.lower() == "black mage" or hero3.lower() == "red mage":
                                print "Here's what spells you have for this hero",hero3_magic
                                hero3_magic_attack = raw_input("PLease type in one of the spells you have")
                        
                            if hero3_magic_attack.lower() != "fire" or hero3_magic_attack.lower() != "sleep" or hero3_magic_attack.lower() != "thunder":
                                print "This spell is not a white magic spell"
                        
                            #Using fire for hero1
                            elif hero3_magic_attack.lower() == "fire":
                                fire_attack = input("Which enemy do want to use this spell on, you can type 1, 2, 3 or 4")
                                #Using fire attack on goblin 1
                                if fire_attack == 1:
                                    goblin1_health -=10
                                    print hero3_name,"attacked goblin 1 for 10 damage"
                                    if goblin1_health <= 0:
                                        print hero3_name,"defeated goblin 1"
                                    elif goblin1_health > 0:
                                        print hero3_name,"did not deal enough damage to defeat goblin1"  
                                #using fire attack on goblin 2
                                elif fire_attack == 2:
                                    goblin2_health -=10
                                    print hero3_name,"attacked goblin 2 for 10 damage"
                                    if goblin2_health <= 0:
                                        print hero3_name,"defeated goblin 2"
                                    elif goblin2_health > 0:
                                        print hero3_name,"did not deal enough damage to defeat goblin1" 
                                #Using fire attack on goblin 3
                                elif fire_attack == 3:
                                    goblin1_health -=10
                                    print hero3_name,"attacked goblin 1 for 10 damage"
                                    if goblin1_health <= 0:
                                        print hero3_name,"defeated goblin 3"
                                    elif goblin1_health > 0:
                                        print hero3_name,"did not deal enough damage to defeat goblin1" 
                        
                            #using sleep for hero3
                            elif hero3_magic_attack.lower() == "sleep":
                                sleep_attack = random.randint(1,10)
                                if sleep_attack == 1 or sleep_attack == 2:
                                    print "All enemies were put to sleep, they will miss their turn"
                                elif sleep_attack == 3 or sleep_attack == 4 or sleep_attack == 5 or sleep_attack == 6 or sleep_attack == 7 or sleep_attack == 8 or sleep_attack == 9 or sleep_attack == 10:
                                    print "The spell didn't work on the enemies"
                                
                            #Using thunder for hero3
                            elif hero3_magic_attack.lower() == "thunder":
                                thunder_attack = input("Which enemy would you like to use this spell on, type 1, 2, 3 or 4")
                                #using thunder on goblin 1
                                if thunder_attack == 1:
                                    goblin1_health -=12
                                    print hero3_name,"dealt 12 damage to goblin 1"
                                    if goblin1_health <= 0:
                                        print hero3_name,"defeated goblin 1"
                                    elif goblin1_health > 0:
                                        print hero3_name,"was not able to defeat goblin 1"
                                #Using thunder on goblin 2
                                elif thunder_attack == 1:
                                    goblin2_health -=12
                                    print hero3_name,"dealt 12 damage to goblin 2"
                                    if goblin2_health <= 0:
                                        print hero3_name,"defeated goblin 2"
                                    elif goblin2_health > 0:
                                        print hero3_name,"was not able to defeat goblin 2"
                            #using thunder on goblin 3
                                if thunder_attack == 3:
                                    goblin3_health -=12
                                    print hero3_name,"dealt 12 damage to goblin 1"
                                    if goblin3_health <= 0:
                                        print hero3_name,"defeated goblin 1"
                                    elif goblin3_health > 0:
                                        print hero3_name,"was not able to defeat goblin 1"
                            
                    #Showing inventory
                    elif hero3_damage.lower() == "item":
                        print "Here's what items you have",inventory   
                        use.inventory = raw_input("What item do you want to use?")
                    
                        if use_inventory.lower() == "potion":
                            heal_potion = raw_input("Who do you want to use this potion on(type hero1, hero2, hero3, or hero4")
                            #Using potion on hero1
                            if heal_potion.lower() == "hero1":
                                if health_for_hero1 == health_for_hero1_with_armor:
                                    print "you cannot use a potion on this because it's health is full"
                                elif health_for_hero1 < health_for_hero1_with_armor:
                                    if "Potion" in inventory:
                                        #Removing the item used
                                        inventory.remove('Potion')
                                        print hero1_name,"healed for 15 points"
                                        health_for_hero1 +=15
                                        #If potion heals more health than intended
                                        if health_for_hero1 > health_for_hero1_with_armor:
                                            health_for_hero1 = 50 
                                            print hero1_name,"(",hero1,"), is now at",health_for_hero1,"hp"
                                    else:
                                        if "Potion" in inventory:
                                            #Removing the item used
                                            inventory.remove('Potion')
                                            print hero1_name,"(",hero1,"), is now at",health_for_hero1,"hp"
                            #Using potion on hero2    
                            elif heal_potion.lower() == "hero2":
                                if health_for_hero2 == health_for_hero2_with_armor:
                                    print "you cannot use a potion on this hero because it's health is full"
                                elif health_for_hero2 < health_for_hero2_with_armor:
                                    if "Potion" in inventory:
                                        #Removing the item used
                                        inventory.remove('Potion')
                                        print hero1_name,"healed for 15 points"
                                        health_for_hero2 +=15
                                    #If potion heals more health than intended
                                        if health_for_hero2 > health_for_hero2_with_armor:
                                            health_for_hero2 = 50
                                            print hero2_name,"(",hero2,"), is now at",health_for_hero2,"hp"
                                    else:
                                        if "Potion" in inventory:
                                            #Removing the item used
                                            inventory.remove('Potion')
                                            print hero2_name,"(",hero2,"), is now at",health_for_hero2,"hp"
                            #Using potion on hero3
                            elif heal_potion.lower() == "hero3":
                                if health_for_hero3 == health_for_hero3_with_armor:
                                    print "you cannot use a potion on this because it's health is full"
                                elif health_for_hero3 < health_for_hero3_with_armor:
                                    if "Potion" in inventory:
                                        #Removing the item used
                                        inventory.remove('Potion')
                                        print hero1_name,"healed for 15 points"
                                        health_for_hero3 +=15
                                    #If potion heals more health than intended
                                        if health_for_hero3 > health_for_hero3_with_armor:
                                            health_for_hero3 = 50
                                            print hero3_name,"(",hero3,"), is now at",health_for_hero3,"hp"
                                    #If hero's health isn't less or more than 50
                                    else:
                                        if "Potion" in inventory:
                                            #Removing the item used
                                            inventory.remove('Potion')
                                            print hero3_name,"(",hero3,"), is now at",health_for_hero3,"hp"
                            #Using potion on hero4
                            elif heal_potion.lower() == "hero4":
                                if health_for_hero4 == health_for_hero4_with_armor:
                                    print "you cannot use a potion on this because it's health is full"
                                elif health_for_hero4 < health_for_hero4_with_armor:
                                    if "Potion" in inventory:
                                        #Removing the item used
                                        inventory.remove('Potion')
                                        print hero4_name,"healed for 15 points"
                                        health_for_hero4 +=15
                                        #If potion heals more health than intended
                                        if health_for_hero4 > health_for_hero4_with_armor:
                                            health_for_hero4 = 50
                                            print hero4_name,"(",hero4,"), is now at",health_for_hero4,"hp"
                                    #If hero's health isn't less or more than 50
                                    else:
                                        if "Potion" in inventory:
                                            #Removing the item used
                                            inventory.remove('Potion')
                                            print hero4_name,"(",hero4,"), is now at",health_for_hero4,"hp"
                        #Using phoenix down
                        elif use_inventory.lower() == "phoenix down":
                            use_phoenix_down = raw_input("Who do you want to use this phoenix down on(type hero1, hero2, hero3, or hero4")
                            #Using phoenix down on hero1
                            if use_phoenix_down.lower() == "hero1":
                                if health_for_hero1 > 0 :
                                    print "You cannot use a phoenix down on",hero1_name,"because their health if full or they are living"
                                elif health_for_hero1 <= 0 :
                                    health_for_hero1 = 20
                                    print "You used phoenix down on",hero1_name,"their health is now at",health_for_hero1
                                    if "Phoenix down" in inventory:
                                        inventory.remove('Phoenix down')
                            #Using phoenix down on hero2
                            elif use_phoenix_down.lower() == "hero2":        
                                if health_for_hero2 > 0 :
                                    print "You cannot use a phoenix down on",hero2_name,"because their health if full"
                                elif health_for_hero2 <= 0 :
                                    health_for_hero2 = 20
                                    print "You used phoenix down on",hero2_name,"their health is now at",health_for_hero2
                                    if "Phoenix down" in inventory:
                                        inventory.remove('Phoenix down')
                                
                            #Using phoenix down on hero3
                            elif use_phoenix_down.lower() == "hero3":        
                                print "You cannot use phoenix down on",hero3_name,"because they are living"
                            #Using phoenix down on hero4
                            elif use_phoenix_down.lower() == "hero4":        
                                if health_for_hero4 == 0:
                                    health_for_hero4 = 20
                                    if "Phoenix down" in inventory:
                                        inventory.remove('Phoenix down')
                                        print hero2_name,"used phoenix down on",hero4_name,". Their health is now",health_for_hero4
                                #If health is full or character is living
                                elif health_for_hero4 > 0:
                                    print "You cannot use a phoenix down on",hero4_name,"because they are at full health"
                
                    #Hero4 attack
                    print "What do you want your fourth hero",hero4,"to do? (You can attack, use a spell, or a item)"
                    hero4_damage = raw_input("What would you like to do? (Type attack, magic or item")
                    if hero4_damage.lower() == "attack":
                        #Choosing which enemy user wants to attack with their second hero
                        enemy = input("Who do you want to attack (type 1 for enemy 1, type 2 for enemy and so on for the amount of enemies you are fighting)")
                        if enemy == 1:
                            if hero4_attack > goblin1_health:
                                damage = hero4_attack - goblin1_health 
                            elif hero4_attack < goblin1_health:
                                damage = goblin1_health = goblin1_health - hero4_attack 
                            if goblin1_health >= 0:
                                print "you did",hero_damage,"to the goblin, you defeated a enemy"
                            elif goblin1_health < 0:
                                print "You did",hero_damage,"to the enemy but didn't defeat them "
                    
                        elif enemy == 2:
                            if hero4_attack > goblin2_health:
                                damage = hero4_attack - goblin2_health 
                            elif hero4_attack < goblin2_health:
                                damage = goblin2_health =  goblin2_health - hero4_attack 
                        
                            if goblin2_health >= 0:
                                print "you did",damage,"to the goblin, you defeated a enemy"
                            elif goblin2_health < 0:
                                print "You did",damage,"to the enemy but didn't defeat them"
                    
                        elif enemy == 3:
                            if hero4_attack > goblin3_health:
                                damage = hero4_attack - goblin3_health 
                            elif hero4_attack < goblin3_health:
                                damage = goblin3_health = goblin3_health - hero4_attack 
                            if goblin3_health >= 0:
                                print "you did",damage,"to the goblin, you defeated a enemy"
                            elif goblin3_health < 0:
                                print "You did",damage,"to the enemy but didn't defeat them"
                        
                    #Hero4 white magic attacks
                    elif hero4_damage.lower() == "white magic":
                        #If user has heros that cannot use white magic
                        if hero4.lower() == "monk" or hero4.lower() == "warrior" or hero4.lower() == "black mage":
                            print hero4_name,"cannot use white magic spells"
                        #If user has hores that can use white magic
                        elif hero4.lower() == "white mage" or hero3.lower() == "red mage":
                            print "Here's what spells you have for this hero",hero4_magic
                            hero4_magic_attack = raw_input("PLease type in one of the spells you have(note that if you are using a red mage, you may see black magic spells. These spells will not work in this attack")
                            
                            if hero4_magic_attack.lower() != "cure" or hero4_magic_attack.lower() != "dia" or hero4_magic_attack.lower() != "protect" or hero4_magic_attack.lower() != "blink":
                                print "This spell is not a white magic spell"
                        
                        #Using cure on hero1
                        elif hero4_magic_attack.lower() == "cure":
                            heal_hero = raw_input("Who do you want to heal?(type hero1, hero2, etc")
                            #Using cure on hero1
                            if heal_hero.lower() == "hero1":
                                if health_for_hero1 == health_for_hero1_with_armor:
                                    print "You cannot heal this hero as there health is max"
                            elif health_for_hero1 < health_for_hero1_with_armor:
                                print hero1_name,"used cure to heal itself by 15 hp"
                                health_for_hero1 += 15
                                #If cure restores more than max health
                                if health_for_hero1 > health_for_hero1_with_armor:
                                    health_for_hero1 = 50
                            #Using cure to heal hero2
                            elif heal_hero.lower() == "hero2":
                                if health_for_hero2 == health_for_hero2_with_armor:
                                    print "You cannot heal",hero2_name
                                #If hero has less health
                                elif health_for_hero2 < health_for_hero2_with_armor:
                                    print hero4_name,"used cure to heal",hero2_name,"by 15 hp"
                                    health_for_hero2 +=15
                                #If cure restores more than max health
                                if health_for_hero2 > health_for_hero2_with_armor:
                                    health_for_hero2 = 50
                            #Using cure to heal hero3
                            elif heal_hero.lower() == "hero3":
                                if health_for_hero3 == health_for_hero3_with_armor:
                                    print "You cannot heal",hero3_name
                            elif health_for_hero3 < health_for_hero3_with_armor: 
                                print hero4_name,"used cure to heal",hero2_name,"by 15 hp"
                                health_for_hero3 +=15
                                #If cure restores more than max health
                                if health_for_hero3 > health_for_hero3_with_armor:
                                    health_for_hero3 = 50 
                                #Using cure to heal hero4
                            elif heal_hero.lower() == "hero4":
                                if health_for_hero4 == health_for_hero4_with_armor:
                                    print "You cannot heal",hero4_name
                            elif health_for_hero4 < health_for_hero4_with_armor:
                                print hero4_name,"used cure to heal themselve by 15 hp"
                                health_for_hero4 +=15
                            #If cure restores more than max health
                                if health_for_hero4 > health_for_hero4_with_armor:
                                    health_for_hero4 = 50
                        
                        #If user wants to use dia
                        elif hero1_magic_attack.lower() == "dia":
                            dia_attack = input("Which enemy do you want to attack out of the 3. You can type 1, 2 or 3")
                            #Using dia on the first goblin
                            if dia_attack == 1:
                                print hero4,"attacked goblin 1 for 20 damage"
                                #Lowering enemy's health
                                goblin1_health -= 20
                            #Using dia on second goblin
                            elif dia_attack == 2:
                                print hero1,"attacked goblin 2 for 20 damage"
                                #Lowering enemy's health
                                goblin2_health -= 20
                            #Using dia on the third goblin
                            elif dia_attack == 3:
                                print hero1,"attacked goblin 2 for 20 damage"
                                #Lowering enemy's health
                                goblin3_health -= 20
                                
                        #If user wants to use protect
                        elif hero1_magic_attack.lower() == "protect":
                            protect_attack = raw_input("Which hero do you want to use this on, you can type hero1, hero2, hero3, or hero4")
                            #Using protect on first hero
                            if protect_attack.lower() == "hero1":
                                print hero1,"used protect to increase their health by 8 points. This spell lasts forever, until the hero's health decreases"
                                health_for_hero1 += 8
                            #Using protect on second hero
                            elif protect_attack.lower() == "hero2":
                                print hero1,"used protect to increase",hero2_name,"health by 8 points. This spell lasts forever, until the hero's health decreases"
                                health_for_hero2 += 8
                            #Using protect on third hero
                            elif protect_attack.lower() == "hero3":
                                print hero1,"used protect to increase their health by 8 points. This spell lasts forever, until the hero's health decreases"
                                health_for_hero3 += 8
                            #Using protect on fourth hero
                            elif protect_attack.lower() == "hero4":
                                print hero1,"used protect to increase",hero4_name,"health by 8 points. This spell lasts forever, unti the hero's health decreases"
                                health_for_hero4 += 8
                        
                        #If user wants to use blink
                        elif hero1_magic_attack.lower() == "blink":
                            print hero1_name,"used blink to increase the chance of not getting attacked by enemies"
                
                #Hero4 black magic attacks
                    elif hero4_damage.lower() == "black magic":
                        if hero4.lower() == "monk" or hero4.lower() == "warrior" or hero4.lower() == "white mage": 
                            print hero4_name,"cannot use black magic spells"
                        #If user has mages that can use white magic
                        elif hero4.lower() == "black mage" or hero4.lower() == "red mage":
                            print "Here's what spells you have for this hero",hero4_magic
                            hero4_magic_attack = raw_input("PLease type in one of the spells you have")
                        
                            if hero4_magic_attack.lower() != "fire" or hero4_magic_attack.lower() != "sleep" or hero4_magic_attack.lower() != "thunder":
                                print "This spell is not a white magic spell"
                        
                            #Using fire for hero1
                            elif hero4_magic_attack.lower() == "fire":
                                fire_attack = input("Which enemy do want to use this spell on, you can type 1, 2, 3 or 4")
                                #Using fire attack on goblin 1
                                if fire_attack == 1:
                                    goblin1_health -=10
                                    print hero4_name,"attacked goblin 1 for 10 damage"
                                    if goblin1_health <= 0:
                                        print hero4_name,"defeated goblin 1"
                                    elif goblin1_health > 0:
                                        print hero4_name,"did not deal enough damage to defeat goblin1"  
                                #using fire attack on goblin 2
                                elif fire_attack == 2:
                                    goblin2_health -=10
                                    print hero4_name,"attacked goblin 2 for 10 damage"
                                    if goblin2_health <= 0:
                                        print hero4_name,"defeated goblin 2"
                                    elif goblin2_health > 0:
                                        print hero4_name,"did not deal enough damage to defeat goblin1" 
                                #Using fire attack on goblin 3
                                elif fire_attack == 3:
                                    goblin1_health -=10
                                    print hero4_name,"attacked goblin 1 for 10 damage"
                                    if goblin1_health <= 0:
                                        print hero4_name,"defeated goblin 3"
                                    elif goblin1_health > 0:
                                        print hero4_name,"did not deal enough damage to defeat goblin1" 
                        
                            #using sleep for hero1
                            elif hero4_magic_attack.lower() == "sleep":
                                sleep_attack = random.randint(1,10)
                                if sleep_attack == 1 or sleep_attack == 2:
                                    print "All enemies were put to sleep, they will miss their turn"
                                elif sleep_attack == 3 or sleep_attack == 4 or sleep_attack == 5 or sleep_attack == 6 or sleep_attack == 7 or sleep_attack == 8 or sleep_attack == 9 or sleep_attack == 10:
                                    print "The spell didn't work on the enemies"
                        
                        
                                
                            #Using thunder for hero1
                            elif hero4_magic_attack.lower() == "thunder":
                                thunder_attack = input("Which enemy would you like to use this spell on, type 1, 2, 3 or 4")
                                #using thunder on goblin 1
                                if thunder_attack == 1:
                                    goblin1_health -=12
                                    print hero4_name,"dealt 12 damage to goblin 1"
                                    if goblin1_health <= 0:
                                        print hero4_name,"defeated goblin 1"
                                    elif goblin1_health > 0:
                                        print hero4_name,"was not able to defeat goblin 1"
                                #Using thunder on goblin 2
                                elif thunder_attack == 1:
                                    goblin2_health -=12
                                    print hero4_name,"dealt 12 damage to goblin 2"
                                    if goblin2_health <= 0:
                                        print hero2_name,"defeated goblin 2"
                                    elif goblin4_health > 0:
                                        print hero4_name,"was not able to defeat goblin 2"
                                #using thunder on goblin 3
                                if thunder_attack == 3:
                                    goblin3_health -=12
                                    print hero4_name,"dealt 12 damage to goblin 1"
                                    if goblin3_health <= 0:
                                        print hero4_name,"defeated goblin 1"
                                    elif goblin3_health > 0:
                                        print hero4_name,"was not able to defeat goblin 1"        
                
                    #Showing inventory
                    elif hero4_damage.lower() == "item":
                        print "Here's what items you have",inventory 
                        use.inventory = raw_input("What item do you want to use?")
                    
                        if use_inventory.lower() == "potion":
                            heal_potion = raw_input("Who do you want to use this potion on(type hero1, hero2, hero3, or hero4")
                            #Using potion on hero1
                            if heal_potion.lower() == "hero1":
                                if health_for_hero1 == health_for_hero1_with_armor:
                                    print "you cannot use a potion on this because it's health is full"
                                elif health_for_hero1 < health_for_hero1_with_armor:
                                    if "Potion" in inventory:
                                        #Removing the item used
                                        inventory.remove('Potion')
                                        print hero1_name,"healed themselves for 15 points"
                                        health_for_hero1 +=15
                                        #If potion heals more health than intended
                                        if health_for_hero1 > health_for_hero1_with_armor:
                                            health_for_hero1 = 50 
                                            print her41_name,"(",hero1,"), is now at",health_for_hero1,"hp"
                                    else:
                                        if "Potion" in inventory:
                                            #Removing the item used
                                            inventory.remove('Potion')
                                            print hero1_name,"(",hero1,"), is now at",health_for_hero1,"hp"
                            #Using potion on hero2    
                            elif heal_potion.lower() == "hero2":
                                if health_for_hero2 == health_for_hero2_with_armor:
                                    print "you cannot use a potion on this hero because it's health is full"
                                elif health_for_hero2 < health_for_hero2_with_armor:
                                    if "Potion" in inventory:
                                        #Removing the item used
                                        inventory.remove('Potion')
                                        print hero1_name,"healed for 15 points"
                                        health_for_hero2 +=15
                                    #If potion heals more health than intended
                                        if health_for_hero2 > health_for_hero2_with_armor:
                                            health_for_hero2 = 50
                                            print hero2_name,"(",hero2,"), is now at",health_for_hero2,"hp"
                                    else:
                                        if "Potion" in inventory:
                                        #Removing the item used
                                            inventory.remove('Potion')
                                            print hero2_name,"(",hero2,"), is now at",health_for_hero2,"hp"
                            #Using potion on hero3
                            elif heal_potion.lower() == "hero3":
                                if health_for_hero3 == health_for_hero3_with_armor:
                                    print "you cannot use a potion on this because it's health is full"
                                elif health_for_hero3 < health_for_hero3_with_armor:
                                    if "Potion" in inventory:
                                        #Removing the item used
                                        inventory.remove('Potion')
                                        print hero1_name,"healed for 15 points"
                                        health_for_hero3 +=15
                                    #If potion heals more health than intended
                                        if health_for_hero3 > health_for_hero3_with_armor:
                                            health_for_hero3 = 50
                                            print hero3_name,"(",hero3,"), is now at",health_for_hero3,"hp"
                                    #If hero's health isn't less or more than 50
                                    else:
                                        if "Potion" in inventory:
                                            #Removing the item used
                                            inventory.remove('Potion')
                                            print hero3_name,"(",hero3,"), is now at",health_for_hero3,"hp"
                            #Using potion on hero4
                            elif heal_potion.lower() == "hero4":
                                if health_for_hero4 == health_for_hero4_with_armor:
                                    print "you cannot use a potion on this because it's health is full"
                                elif health_for_hero4 < health_for_hero4_with_armor:
                                    if "Potion" in inventory:
                                        #Removing the item used
                                        inventory.remove('Potion')
                                        print hero4_name,"healed for 15 points"
                                        health_for_hero4 +=15
                                        #If potion heals more health than intended
                                        if health_for_hero4 > health_for_hero4_with_armor:
                                            health_for_hero4 = 50
                                            print hero4_name,"(",hero4,"), is now at",health_for_hero4,"hp"
                                    #If hero's health isn't less or more than 50
                                    else:
                                        if "Potion" in inventory:
                                            #Removing the item used
                                            inventory.remove('Potion')
                                            print hero4_name,"(",hero4,"), is now at",health_for_hero4,"hp"
                            #Using phoenix down
                            elif use_inventory.lower() == "phoenix down":
                                use_phoenix_down = raw_input("Who do you want to use this phoenix down on(type hero1, hero2, hero3, or hero4")
                                #Using phoenix down on hero1
                                if use_phoenix_down.lower() == "hero1":
                                    if health_for_hero1 > 0 :
                                        print "You cannot use a phoenix down on",hero1_name,"because their health if full or they are living"
                                elif health_for_hero1 <= 0 :
                                    health_for_hero1 = 20
                                    print "You used phoenix down on",hero1_name,"their health is now at",health_for_hero1
                                    if "Phoenix down" in inventory:
                                        inventory.remove('Phoenix down')
                            #Using phoenix down on hero2
                            elif use_phoenix_down.lower() == "hero2":        
                                if health_for_hero2 > 0 :
                                    print "You cannot use a phoenix down on",hero2_name,"because their health if full"
                                elif health_for_hero2 <= 0 :
                                    health_for_hero2 = 20
                                    print "You used phoenix down on",hero2_name,"their health is now at",health_for_hero2
                                    if "Phoenix down" in inventory:
                                        inventory.remove('Phoenix down')
                                
                            #Using phoenix down on hero3
                            elif use_phoenix_down.lower() == "hero3":        
                                if health_for_hero3 > 0 :
                                    print "You cannot use a phoenix down on",hero3_name,"because their health if full"
                                elif health_for_hero3 <= 0 :
                                    health_for_hero3 = 20
                                    print "You used phoenix down on",hero3_name,"their health is now at",health_for_hero3
                                    if "Phoenix down" in inventory:
                                        inventory.remove('Phoenix down')
                                #If health is full or character is living
                                elif health_for_hero4 > 0:
                                    print "You cannot use a phoenix down on",hero3_name,"because they are at full health"
                            #Using phoenix down on hero4
                            elif use_phoenix_down.lower() == "hero4":        
                                print "You cannot use phoenix down on this hero because they are alive"
                    
                    
                
                    #Enemy attack
                    if sleep_attack == 1 or sleep_attack == 2:
                        continue
                    enemy_attack = random.randint(1,6)
                    #Goblin1 attack on hero1
                    if enemy_attack == 1:
                        if goblin1_damage > health_for_hero1:
                            enemy_damage= goblin1_damage - health_for_hero1
                        if health_for_hero1 <= 0:
                            print "Your",hero1,"(",hero1_name,") died, you can use a phoenix down to revive your fallen hero"
                        elif health_for_hero1 > 0:
                            print "The first goblin attacked your",hero1,"and lost",enemy_damage,"health"
                        elif health_for_hero1 <= 5 and health_for_hero1 <= 10:
                            print hero1,"took",enemy_damage,"they are now at",health_for_hero1,"hp, you might want to use a potion"
                    #goblin1 attack on hero2
                    if enemy_attack == 2:
                        if goblin1_damage > health_for_hero2:
                            enemy_damage= goblin1_damage - health_for_hero2
                        if health_for_hero2 <= 0:
                            print "Your",hero2,"(",hero2_name,") died, you can use a phoenix down to revive your fallen hero"
                        elif health_for_hero2 > 0:
                            print "The first goblin attacked your",hero2,"and lost",enemy_damage,"health"
                        elif health_for_hero2 <= 5 and health_for_hero2 <= 10:
                            print hero2,"took",enemy_damage,"they are now at",health_for_hero2,"hp, you might want to use a potion"
                    #goblin1 attack on hero3
                    if enemy_attack == 3:
                        if goblin1_damage > health_for_hero3:
                            enemy_damage= goblin1_damage - health_for_hero3
                        if health_for_hero3 <= 0:
                            print "Your",hero3,"(",hero3_name,") died, you can use a phoenix down to revive your fallen hero"
                        elif health_for_hero3 > 0:
                            print "The first goblin attacked your",hero1,"and lost",enemy_damage,"health"
                        elif health_for_hero3 <= 5 and health_for_hero3 <= 10:
                            print hero3,"took",enemy_damage,"they are now at",health_for_hero3,"hp, you might want to use a potion"
                    #goblin1 attack on hero4
                    if enemy_attack == 4:
                        if goblin1_damage > health_for_hero4:
                            enemy_damage= goblin1_damage - health_for_hero4
                        if health_for_hero4 <= 0:
                            print "Your",hero4,"(",hero4_name,") died, you can use a phoenix down to revive your fallen hero"
                        elif health_for_hero4 > 0:
                            print "The first goblin attacked your",hero4,"and lost",enemy_damage,"health"
                        elif health_for_hero4 <= 5 and health_for_hero4 <= 10:
                            print hero4,"took",enemy_damage,"they are now at",health_for_hero4,"hp, you might want to use a potion"
                    if enemy_attack == 5 or enemy_attack == 6:
                        print "Goblin 1 missed their attack"
                    
                    #Goblin 2 damage
                    enemy_attack2 = random.randint(1,6)
                    #Goblin2 attack on hero1
                    if enemy_attack2 == 1:
                        if goblin2_damage > health_for_hero1:
                            enemy_damage= goblin2_damage - health_for_hero1
                        if health_for_hero1 <= 0:
                            print "Your",hero1,"(",hero1_name,") died, you can use a phoenix down to revive your fallen hero"
                        elif health_for_hero1 > 0:
                            print "The second goblin attacked your",hero1,"and lost",enemy_damage,"health"
                        elif health_for_hero1 <= 5 and health_for_hero1 <= 10:
                            print hero1,"took",enemy_damage,"they are now at",health_for_hero1,"hp, you might want to use a potion"
                    #goblin2 attack on hero2
                    if enemy_attack == 2:
                        if goblin2_damage > health_for_hero2:
                            enemy_damage= goblin2_damage - health_for_hero2
                        if health_for_hero2 <= 0:
                            print "Your",hero2,"(",hero2_name,") died, you can use a phoenix down to revive your fallen hero"
                        elif health_for_hero2 > 0:
                            print "The second goblin attacked your",hero2,"and lost",enemy_damage,"health"
                        elif health_for_hero2 <= 5 and health_for_hero2 <= 10:
                            print hero2,"took",enemy_damage,"they are now at",health_for_hero2,"hp, you might want to use a potion"
                    #goblin2 attack on hero3
                    if enemy_attack == 3:
                        if goblin2_damage > health_for_hero3:
                            enemy_damage= goblin2_damage - health_for_hero3
                        if health_for_hero3 <= 0:
                            print "Your",hero3,"(",hero3_name,") died, you can use a phoenix down to revive your fallen hero"
                        elif health_for_hero3 > 0:
                            print "The second goblin attacked your",hero1,"and lost",enemy_damage,"health"
                        elif health_for_hero3 <= 5 and health_for_hero3 <= 10:
                            print hero3,"took",enemy_damage,"they are now at",health_for_hero3,"hp, you might want to use a potion"
                    #goblin2 attack on hero4
                    if enemy_attack == 4:
                        if goblin2_damage > health_for_hero4:
                            enemy_damage= goblin2_damage - health_for_hero4
                        if health_for_hero4 <= 0:
                            print "Your",hero4,"(",hero4_name,") died, you can use a phoenix down to revive your fallen hero"
                        elif health_for_hero4 > 0:
                            print "The second goblin attacked your",hero4,"and lost",enemy_damage,"health"
                        elif health_for_hero4 <= 5 and health_for_hero4 <= 10:
                            print hero4,"took",enemy_damage,"they are now at",health_for_hero4,"hp, you might want to use a potion"
                    if enemy_attack == 5 or enemy_attack == 6:
                        print "Goblin 2 missed their attack"
                        
                    #Goblin 3 damage
                    enemy_attack3 = random.randint(1,6)
                    #Goblin3 attack on hero1
                    if enemy_attack3 == 1:
                        if goblin3_damage > health_for_hero1:
                            enemy_damage= goblin3_damage - health_for_hero1
                        if health_for_hero1 <= 0:
                            print "Your",hero1,"(",hero1_name,") died, you can use a phoenix down to revive your fallen hero"
                        elif health_for_hero1 > 0:
                            print "The third goblin attacked your",hero1,"and lost",enemy_damage,"health"
                        elif health_for_hero1 <= 5 and health_for_hero1 <= 10:
                            print hero1,"took",enemy_damage,"they are now at",health_for_hero1,"hp, you might want to use a potion"
                    #goblin2 attack on hero2
                    if enemy_attack == 2:
                        if goblin3_damage > health_for_hero2:
                            enemy_damage= goblin3_damage - health_for_hero2
                        if health_for_hero2 <= 0:
                            print "Your",hero2,"(",hero2_name,") died, you can use a phoenix down to revive your fallen hero"
                        elif health_for_hero2 > 0:
                            print "The third goblin attacked your",hero2,"and lost",enemy_damage,"health"
                        elif health_for_hero2 <= 5 and health_for_hero2 <= 10:
                            print hero2,"took",enemy_damage,"they are now at",health_for_hero2,"hp, you might want to use a potion"
                    #goblin2 attack on hero3
                    if enemy_attack == 3:
                        if goblin3_damage > health_for_hero3:
                            enemy_damage= goblin3_damage - health_for_hero3
                        if health_for_hero3 <= 0:
                            print "Your",hero3,"(",hero3_name,") died, you can use a phoenix down to revive your fallen hero"
                        elif health_for_hero3 > 0:
                            print "The third goblin attacked your",hero1,"and lost",enemy_damage,"health"
                        elif health_for_hero3 <= 5 and health_for_hero3 <= 10:
                            print hero3,"took",enemy_damage,"they are now at",health_for_hero3,"hp, you might want to use a potion"
                    #goblin2 attack on hero4
                    if enemy_attack == 4:
                        if goblin3_damage > health_for_hero4:
                            enemy_damage= goblin3_damage - health_for_hero4
                        if health_for_hero4 <= 0:
                            print "Your",hero4,"(",hero4_name,") died, you can use a phoenix down to revive your fallen hero"
                        elif health_for_hero4 > 0:
                            print "The third goblin attacked your",hero4,"and lost",enemy_damage,"health"
                        elif health_for_hero4 <= 5 and health_for_hero4 <= 10:
                            print hero4,"took",enemy_damage,"they are now at",health_for_hero4,"hp, you might want to use a potion"
                    if enemy_attack == 5 or enemy_attack == 6:
                        print "Goblin 3 missed their attack"
                    #If user's party died 
                    if health_for_hero1 == 0 and health_for_hero2 == 0 and health_for_hero3 == 0 and health_for_hero4 == 0:
                        print "your party died and will respawn in town with max health"
                        break
                    #If user's party wins
                    if goblin1_health == 0 and goblin2_health == 0 and goblin3_health == 0:
                        print "Your party eliminated the goblins and was able to win.\nUnfortunatly, that is all that is in this pre-alpha for now. But more content will be added on. Such as the ability to have different numbers of eneimies spawn"
                        break
                        