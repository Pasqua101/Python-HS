def knightMove(a):
    """kinghtMove(a) : gets the letter and number entered by the user and moves it across the board"""

    if user_move_vert == move_vert1:
        if user_move_hori == move_hori2:
            x = ("You moved up to (f,8)")
            return x

    if user_move_vert == move_vert2:
        if user_move_hori == move_hori1:
            x = ("You moved down to (b,5)")
            return x


x = ''
y = ''
# Determining how many spaces the knight moves
move_vert1 = 1
move_hori1 = 1

move_vert2 = 2
move_hori2 = 2

# Asking user how many spaces they want to move by
user_move_vert = 0

user_move_hori = 0

# Asking the user the way they want to move

user_move_vert = int(input("How to do you want to move vertically?(You can move by 1 or 2 spaces) "))

user_move_hori = int(input("How to do you want to move horizontally? (You can move by 1 or 2 spaces if you already chose 2 or 1, you may not choose that number again.) "))

print(knightMove(x))