import gameboard
import player

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")
# Create a new GameBoard called board - pulling GameBoard functions and creating game board object in app.py
board = gameboard.GameBoard()
# Create a new Player called played starting at position 3,2 - pulling player class to create a player object in app.py
played = player.Player(3, 2)


# Move the player through the board
#  the if statements call the movement functions using played variable to move player around the board.
# played and board variables represent objects.
# second if statements are put there to catch when theres a error and player moves where its not supposed to be
# putting -1 and +1 are to represent players movement in player.py 
while True:
    board.printBoard(played.rowPosition, played.columnPosition)
    selection = input("Make a move: ")
    if(selection == 'w'):
        if(board.checkMove(played.rowPosition -1, played.columnPosition)):
            played.moveUp()
        
    elif(selection == 's'):
        if(board.checkMove(played.rowPosition +1, played.columnPosition)):
            played.moveDown()

    elif(selection == 'a'):
        if(board.checkMove(played.rowPosition, played.columnPosition -1)):
            played.moveLeft()

    elif(selection == 'd'):
        if(board.checkMove(played.rowPosition, played.columnPosition +1)):
            played.moveRight()
    

    # Check if the player has won, if so print a message and break the loop!- exactly what you said lol
    if(board.checkWin(played.rowPosition, played.columnPosition)):
        print("Winner!!")
        break