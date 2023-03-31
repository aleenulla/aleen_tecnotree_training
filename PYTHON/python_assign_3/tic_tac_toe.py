def print_board(board):
    print("-------------")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("-------------")

def check_win(board, mark):
    if (board[0] == board[1] == board[2] == mark or
        board[3] == board[4] == board[5] == mark or
        board[6] == board[7] == board[8] == mark or
        board[0] == board[3] == board[6] == mark or
        board[1] == board[4] == board[7] == mark or
        board[2] == board[5] == board[8] == mark or
        board[0] == board[4] == board[8] == mark or
        board[2] == board[4] == board[6] == mark):
        return True
    return False

def tic_tac_toe():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    current_player = "X"
    game_over = False
    
    while not game_over:
        print_board(board)
        print("It's " + current_player + "'s turn.")
        choice = input("Choose a position from 1-9: ")
        choice = int(choice) - 1
        
        if board[choice] == " ":
            board[choice] = current_player
            if check_win(board, current_player):
                print_board(board)
                print(current_player + " wins!")
                game_over = True
            elif " " not in board:
                print_board(board)
                print("It's a tie!")
                game_over = True
            else:
                if current_player == "X":
                    current_player = "O"
                else:
                    current_player = "X"
        else:
            print("That position is already taken. Try again.")
            
tic_tac_toe()
