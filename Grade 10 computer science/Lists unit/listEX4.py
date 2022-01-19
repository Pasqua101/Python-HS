
import random

Tail_of_snakes =    [14, 20, 39, 88, 66, 69, 79, 84]
Head_of_the_snake = [ 3, 15, 33, 36, 53, 58, 67, 71]
bottom_of_ladders = [ 6, 24, 30, 49, 82]
Top_of_ladder =     [17, 26, 44, 62, 86]

player1_spot_on_board = 0
player2_spot_on_board = 0

while (player1_spot_on_board < 90 and player2_spot_on_board < 90):
    
    #Roll for player 1 
    roll1 = random.randint(1,6)
    player1_spot_on_board = player1_spot_on_board + roll1
    print "Player 1 rolled",roll1,"and moved to spot",player1_spot_on_board
    
    
    
    #Ladders for player 1
    x = 0
    while (x <= 4):
        if bottom_of_ladders[x] == player1_spot_on_board:
            player1_spot_on_board = Top_of_ladder[x]
            print "Player 1 climbed a ladder to spot",player1_spot_on_board
            break
        x +=1
    
    #Snakes for player 1
    x = 0
    while (x <= 7):
        if Tail_of_snakes[x] == player1_spot_on_board:
            player1_spot_on_board = Head_of_the_snake[x]
            print "Player 1 slid down a snake",player1_spot_on_board
            break
        x +=1
    
    #Roll for player 2
    press_enter= raw_input("Press enter to roll: ")
    roll2 = random.randint(1,6)
    print "You rolled a",roll2
    player2_spot_on_board = player2_spot_on_board + roll2
    print "You moved to spot",player2_spot_on_board
    
    #Ladders for player 2
    x = 0
    while (x <= 4):
        if bottom_of_ladders[x] == player2_spot_on_board:
            player2_spot_on_board = Top_of_ladder[x]
            print "You climbed a ladder to spot",player2_spot_on_board
            break
        x +=1
    
    #Snakes for player 2
    x = 0
    while (x <= 7):
        if Tail_of_snakes[x] == player2_spot_on_board:
            player2_spot_on_board = Head_of_the_snake[x]
            print "You slid down a snake",player2_spot_on_board
            break
        x +=1

if player1_spot_on_board >= 90:
    print "player 1 has won the game"
if player2_spot_on_board >= 90:
    print "You have won the game"