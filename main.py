import os
print("Welcome to Tic Tac Toe ")
game_on = True

def pick_marker():
  marker = " "
  
  while not (marker == "X" or marker == "O"):
    marker = input("Player 1 do you want to X or O: ").upper()
    
  if marker == 'X':
    return ('X', 'O')
  else:
    return ('O', 'X')

def display(board):
  
  os.system("clear")
  print("          |            | ")
  print("        "+ board[7]+ " |      " + board[8] + "     | " + board[9])
  print("          |            | ")
  print("    ----------------------------")
  print("          |            | ")
  print("        "+ board[4]+ " |      " + board[5] + "     | " + board[6])
  print("          |            | ")
  print("    ----------------------------")
  print("          |            | ")
  print("        "+ board[1]+ " |      " + board[2] + "     | " + board[3])
  print("          |            | ")
  
def check_winner(board, marker):
    return (
      (board[1] == board[2] == board[3] == marker) or (board[4] == board[5] == board[6] == marker) or (board[7] == board[8] == board[9] == marker) or ##row
      (board[1] == board[4] == board[7] == marker) or (board[8] == board[5] == board[2] == marker) or (board[9] == board[6] == board[3] == marker) or # column
      (board[7] == board[5] == board[3] == marker) or (board[1] == board[5] == board[9] == marker) #diagonal
    )


def game_play(player1, player2, board):
  play = True
  position = 0
  
  while play and position not in list(range(1, 10)):  
    while True:
      try:
        position1 = int(input("Player 1 Choose your next position (1-9): "))
        while board[position1] != " ":  
          print("This position is already taken")
          position1 = int(input("Player 1 Choose your next position (1-9): "))
        board[position1] = player1
      except:
        print("You entered the wrong input")
      else:
        break
    display(board)
    if " " not in board[1:11]:
        print("This is a Tie game")
        break
      
    if check_winner(board, player1):
      print("Player 1 wins the game!")
      play = False
      break
    else:
      pass
    
    while True:
      try:
        position2 = int(input("Player 2 Choose your next position (1-9): "))
        while board[position2] != " ":
          print("This position is already taken")
          position2 = int(input("Player 2 Choose your next position (1-9): "))
        board[position2] = player2
      except:
        print("You entered the wrong input")
      else:
        break
    display(board)
    if check_winner(board, player2):
      print("Player 2 wins the game!")
      play = False
    else:
      pass
    
    
while game_on:
  board = [" "]*10
  player1, player2 = pick_marker()
  display(board)
  game_play(player1, player2, board)
  
  replay = " "
  while not (replay == 'yes' or replay == 'no'):
    replay = input("Do you wish to replay? Enter Yes or No: ").lower()
    if replay == 'yes':
      os.system("clear")
      break
    else:
      game_on = False
      break
    
  
    
    
  



