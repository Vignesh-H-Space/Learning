board = [" "] * 9

def show():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

def move(player):
    while True:
        try:
            pos = int(input(f"{player} choose 1-9: ")) - 1
            if pos < 0 or pos > 8:
                print("Invalid range!")
            elif board[pos] != " ":
                print("Already taken!")
            else:
                board[pos] = player
                break
        except:
            print("Enter a number!")

def show():
    for i in range(9):
        print(board[i] if board[i] != " " else i+1, end=" ")
        if (i + 1) % 3 == 0:
            print()

def check(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(board[i] == player for i in w) for w in wins)

while True:
    show()
    move("X")
    show()
    move("O")
    if check("X"):
        show()
    print("X wins!")
    break
    
