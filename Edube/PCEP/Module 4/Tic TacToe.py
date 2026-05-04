board = [" "] * 9

def show():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

def move(player):
    pos = int(input("Choose 1-9: ")) - 1
    if board[pos] == " ":
        board[pos] = player

while True:
    show()
    move("X")
    show()
    move("O")