board = [".", ".", ".",
         ".", ".", ".",
         ".", ".", "."]

game_now = True
winner = None
current_player = "x"

def game():
    view_board()
    while game_now:
        handle_turn(current_player)
        check_game_over()
        flip_player()

    if winner == "o" or winner == "x":
        print("win")
    elif winner == None:
        print("tie")

def view_board():
    print(board[0]+" | "+board[1]+" | "+board[2]+"   1 | 2 | 3")
    print(board[3]+" | "+board[4]+" | "+board[5]+"   4 | 5 | 6")
    print(board[6]+" | "+board[7]+" | "+board[8]+"   7 | 8 | 9")

def handle_turn(player):
    valid = False
    position = input("Please you should choose the position (1-9): ")
    while (not valid):
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Please you should choose the position (1-9):  ")
        position = int(position) - 1
        if board[position] == ".":
            valid = True
        else:
            print("Please go again")
    board[position] = player
    view_board()

def check_game_over():
    check_for_winner()
    check_for_tie()

def check_for_winner():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

def check_rows():
    global game_now
    row_1 = board[0] == board[1] == board[2] != "."
    row_2 = board[3] == board[4] == board[5] != "."
    row_3 = board[6] == board[7] == board[8] != "."
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None

def check_columns():
  global game_now
  column_1 = board[0] == board[3] == board[6] != "."
  column_2 = board[1] == board[4] == board[7] != "."
  column_3 = board[2] == board[5] == board[8] != "."
  if column_1 or column_2 or column_3:
    game_still_going = False
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  else:
    return None


def check_diagonals():
  global game_now
  diagonal_1 = board[0] == board[4] == board[8] != "."
  diagonal_2 = board[2] == board[4] == board[6] != "."
  if diagonal_1 or diagonal_2:
    game_now = False
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  else:
    return None

def check_for_tie():
  global game_now
  if "." not in board:
    game_now = False
    return True
  else:
    return False

def flip_player():
  global current_player
  if current_player == "x":
    current_player = "o"
  elif current_player == "o":
    current_player = "x"

    game()


