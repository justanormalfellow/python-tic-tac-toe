import random

victory = False
played = []
board = ['1', '2', '3', '4', '5', '6' ,'7', '8', '9']

def drawBoard():
    print(f"""
              {board[0]}|{board[1]}|{board[2]}
              {board[3]}|{board[4]}|{board[5]}
              {board[6]}|{board[7]}|{board[8]}
""")
    playerInput()

def playerInput():
    global victory
    turn = input("Select a number: ")

    if turn in played:
        print("It's already been selected!")
        playerInput()

    for i, item in enumerate(board):
        if item == turn:
            board.pop(i)
            board.insert(i, "x")

    played.append(turn)
    checkwin()
    while len(played) <= 8 and not victory:
        computerTurn()

def computerTurn():
    global victory
    possibilities = [str(i) for i in range(1, 10) if str(i) not in played]

    comp_turn = random.choice(possibilities)
    for i, item in enumerate(board):
         if item == comp_turn:
            board.pop(i)
            board.insert(i, "o")

    played.append(comp_turn)
    checkwin()
    drawBoard()

def checkwin():
    global victory
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == 'x':
            print("Player wins!")
            victory = True
        elif board[i] == board[i + 1] == board[i + 2] == 'o':
            print("Machine wins :(")
            victory = True

    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == 'x':
            print("Player wins!")
            victory = True
        elif board[i] == board[i + 3] == board[i + 6] == 'o':
            print("Machine wins :(")
            victory = True

    # Check diagonals
    if board[0] == board[4] == board[8] == 'x' or board[2] == board[4] == board[6] == 'x':
        print("Player wins!")
        victory = True
    elif board[0] == board[4] == board[8] == 'o' or board[2] == board[4] == board[6] == 'o':
        print("Machine wins :(")
        victory = True

    return False

drawBoard()



    








