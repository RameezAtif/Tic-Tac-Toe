import random

board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']
currentPlayer = "X"
winner = None
gameRunning = True




# Printing the board

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" * 9)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 9)
    print(board[6] + " | " + board[7] + " | " + board[8])

# Taking player input
def playerInput(board):
    while True:
        if currentPlayer == "X":
            inp = int(input(f"Enter a number 1-9 \033[1;34m Player (X) \033[0;0m : ")) 
        else:
            inp = int(input(f"Enter a number 1-9 \033[1;31m Player (0) \033[0;0m : "))
        if inp >= 1 and inp <= 9 and board[inp-1] == "-":
            board[inp-1] = currentPlayer
            break
        else:
            if currentPlayer == "X":
                print(f"Oops! Try again! Player - \033[1;34m Player (X) \033[0;0m ! ")
            else:
                print(f"Oops! Try again! Player - \033[1;31m Player (0) \033[0;0m ! ")
            printBoard(board)


# Check for win or tie
def checkHorizontal(board):
    global winner
    if (board[0] == board[1] == board[2] and board[0] != "-") or (board[3] == board[4] == board[5] and board[3] != "-") or (board[6] == board[7] == board[8] and board[6] != "-"):
        winner = currentPlayer
        return True
def checkRow(board):
    global winner
    if (board[0] == board[3] == board[6] and board[0] != "-") or (board[1] == board[4] == board[7] and board[1] != "-") or (board[2] == board[5] == board[8] and board[2] != "-"):
        winner = currentPlayer
        return True
def checkDiagonal(board):
    global winner
    if (board[0] == board[4] == board[5] and board[0] != "-") or (board[2] == board[4] == board[6] and board[2] != "-"):
        winner = currentPlayer
        return True
def checkTie(board):
    global gameRunning
    global winner
    if "-" not in board and winner == None:
        printBoard(board)
        print("Its a tie")
        gameRunning = False

def checkWin():
   
    if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
        print(f"The winner is {winner}")
       

# Switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def computer(board):
    while currentPlayer == "O":
        randomPosition = random.randint(0,8)
        if board[randomPosition] == "-":
            board[randomPosition] = "O"
           
            switchPlayer()
           
            


def playerVsPlayer(board):
    
    while gameRunning:
        printBoard(board)
        if winner != None:
            break
        playerInput(board)
        checkWin()
        checkTie(board)
        switchPlayer()



def playerVsComp(board):


    while gameRunning:
        printBoard(board)
        if winner != None:
            break
        playerInput(board)
        checkWin()
        checkTie(board)
        switchPlayer()
        computer(board)
        checkWin()
        checkTie(board)
        
        
        





choice = input("Please select a game mode \n singleplayer -> player vs computer \n multiplayer -> player vs player \n")
if choice == "multiplayer":
    playerVsPlayer(board)
elif choice == "singleplayer":
    playerVsComp(board)
else:
    print("Please select a valid game mode")

