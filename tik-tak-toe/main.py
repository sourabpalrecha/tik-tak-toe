#--------global variables-------

#Game board
board = [ "-" , "-" ,"-",
          "-" , "-" ,"-",
          "-" , "-" ,"-"]

#game is still going
game_still_going = True

#whos the winner
winner = None

#current player
current_player="X"


def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
    
    
    
#the game play
def play_game():
    
  display_board()
  while game_still_going:

     handel_turn(current_player)

     check_if_gameover()

     flip_player()
 
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print(" Its a Tie.")





def handel_turn(player):
  print(player +"'s Turn")
  position = input("Enter a Position from 1-9 :")
  valid = False
  while not valid:

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("invaid input! Please Enter a Position from 1 to 9 :")
      
    position = int(position) - 1
    
    if board[position] == "-":
      valid = True
    else:
      print("worng position, try again")

  board[position] = player  
  display_board()


def check_if_gameover():
    check_if_win()
    check_if_tie()


def check_if_win():
  global winner
  #check rows
  row_winner = check_rows()
  #check columns
  columns_winner = check_columns()
  #check diagonals
  diagonal_winner = check_diagonals()
  if row_winner:
   winner = row_winner
  elif columns_winner:
   winner = columns_winner
  elif diagonal_winner:
   winner = diagonal_winner
  else:
   winner = None
  return


def check_rows():
  # Set global variables
  global game_still_going
  # Check if any of the rows have all the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  # Return the winner
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 
  # Or return None if there was no winner
  else:
    return None






def check_columns():
  global game_still_going

  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"

  if column_1 or column_2 or column_3:
    game_still_going = False
    
  #Return the winner either X or O
  if column_1:
    return board[0]
  if column_2:
    return board[1]
  if column_3:
    return board[2]





def check_diagonals():
  global game_still_going

  diagonal1 = board[0] == board[4] == board[8] != "-"
  diagonal2 = board[2] == board[4] == board[6] != "-"
 

  if diagonal1 or diagonal2:
    game_still_going = False
    
  #Return the winner either X or O
  if diagonal1:
    return board[4]
  if diagonal2:
    return board[4]
  
  return



def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False
  return

def flip_player():
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X" 
  return

play_game() 