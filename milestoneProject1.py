def display_board(board):
  #print('\n'*100)

  print('   |   |')
  print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
  print('   |   |')

def markPlayers(p,mark):
  mark_players = {'Player1':'', 'Player2':''}
  if p == 1:
    mark_players['Player1'] = mark
    if mark == 'X':
      mark_players['Player2'] = 'O'
    else:
      mark_players['Player2'] = 'X'
  else:
    mark_players['Player2'] = mark
    if mark == 'X':
      mark_players['Player1'] = 'O'
    else:
      mark_players['Player1'] = 'X'
  return mark_players

def space_check(board,position):
  return board[position] == ' '

def full_board_check(board):
  for i in range(1,len(board)):
    if space_check(board,i):
      return True
  return False

def win_check(board,mark):
  return ((board[1] == mark and board[2] == mark and board[3] == mark) or
  (board[4] == mark and board[5] == mark and board[6] == mark) or
  (board[7] == mark and board[8] == mark and board[9] == mark) or
  (board[1] == mark and board[5] == mark and board[9] == mark) or
  (board[3] == mark and board[5] == mark and board[7] == mark) or
  (board[1] == mark and board[4] == mark and board[7] == mark) or
  (board[2] == mark and board[5] == mark and board[8] == mark) or
  (board[3] == mark and board[6] == mark and board[9] == mark))

def update_board(board,mark,position):
  board[position] = mark
  return board

def switch_player(player):
  if player == 'Player1':
    return 'Player2'
  else:
    return 'Player1'

def choose_position(board, current_player, mark):
  position = int(input("{a}: Where do you want to place your {b}.\n\n".format(a = current_player, b = mark)))
  print("\n")
  while position not in [1,2,3,4,5,6,7,8,9] or not(space_check(board,position)):
    position = int(input("Choose a free position between (1..9).\n\n"))
  return position



