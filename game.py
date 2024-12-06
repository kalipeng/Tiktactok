import numpy

user_move = input("Please enter your move as x,y coordinates. i.e. 1,2: ")
print(f"You entered: {user_move}")



board = [['O', 'X', 'X'],
         ['X', 'X', 'O'],
         ['O', 'X', 'X']]

def win():
    for x in range(3):
        if board[x][0] == board[x][1] == board[x][2]:  # board [0][0]first row, first element
            return board[x][0] # either X or O

    for y in range(3):
        if board[0][y] == board[1][y] == board[2][y]:
            return board[0][y]

    for x in range(0, 3, 2):
        if board[x][0] == board[1][1] == board[2-x][2]:
            return board[x][0]
    return False

if win() is not False:
    print(win()+" won")
