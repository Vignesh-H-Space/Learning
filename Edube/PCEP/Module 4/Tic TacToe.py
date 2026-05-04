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

while True:
    show()
    move("X")
    show()
    move("O")