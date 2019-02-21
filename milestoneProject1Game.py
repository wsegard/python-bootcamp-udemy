from random import randint
from milestoneProject1 import markPlayers
from milestoneProject1 import space_check
from milestoneProject1 import full_board_check
from milestoneProject1 import win_check
from milestoneProject1 import display_board
from milestoneProject1 import update_board
from milestoneProject1 import switch_player
from milestoneProject1 import choose_position
#from milestoneProject1 import replay

while True:

  #Choose randomly who starts the game

  p = randint(1,2)
  print("Player {} will start first\n".format(p))

  #Ask player his mark ('X' or 'O')

  mark = ''
  mark = input("Player {}: Choose between X or O.\n\n".format(p))
  while mark != 'X' and mark != 'O':
    mark = ''
    print("You need to choose between X or O.")
    mark = input("Please choose again!\n").upper()

  mark_players = markPlayers(p,mark)

  #Initialise the board, mark and player

  board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
  current_player = "Player{}".format(p)
  mark = mark_players[current_player]

  #Start the game
  print("\n")
  display_board(board)
  print("\n")

  while not(win_check(board,mark)) and full_board_check(board):
    position = choose_position(board,current_player,mark)
    update_board(board,mark,position)
    print("\n")
    display_board(board)
    print("\n")
    if win_check(board,mark):
      print("{} has won!!\n\n".format(current_player))
      break
    elif not(full_board_check(board)):
      print("That's a tie\n\n")
      break
    else:
      current_player = switch_player(current_player)
      mark = mark_players[current_player]

  answer = input("Do you want to play again: yes or no?\n\n").lower()
  print('\n')
  while answer not in ['yes','no']:
    answer = input("I did not understand what you said.\nDo you want to play again: yes or no?\n\n").lower()
  if answer == 'no':
    break

print('\n')
print('Goodbye')
