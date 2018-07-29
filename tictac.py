import random

class tic_tac_toe:

  def __init__(self):
    self.game_is_playing = False
    # create game board
    self.board = [' '] * 9 # empty board currently

  def play(self):
    print("Welcome to Tic-Tac-Toe! Choose a player to be Player 1 and Player 2. Player 1 wil be x's, and player 2 will be o's.")
    print("Player 1 will go first.")

    self.game_is_playing = True
    player = 1 # this will alternate between 1 and 2 depending on whose turn it is

    while self.game_is_playing:
      self.print_board()
      print("Player " + str(player) + ", it's your turn.")
      move = self.get_player_move()
      self.move(player, move-1)

      if self.is_winner(player):
        self.print_board()
        print("Player " + str(player) + " has won!")
        self.game_is_playing = False

      elif self.board_is_full():
        self.print_board()
        print("Cat's game!")
        self.game_is_playing = False

      # if no winners, switch whose turn it is
      player = self.switch_player(player)

  def print_board(self):
    print('   |   |')
    print(' ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
    print('-----------')
    print(' ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
    print('   |   |')
    print('-----------')
    print(' ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])
    print('   |   |')

  def get_player_move(self):
    move = input("Where would you like to move? (1-9) ")
    while not move.isdigit():
      move = input("Please enter a valid move: ")

    # if it can be converted to an integer...
    while int(move) not in {1,2,3,4,5,6,7,8,9} or not self.space_is_free(int(move)):
      move = input("Please enter a valid move: ")
    return int(move)

  def move(self, player, move): #update game board
    piece = ""
    if player == 1:
      piece = "x"
    else:
      piece = "o"
    self.board[move] = piece

  def space_is_free(self, move): #checks if a space on the board is free
    return self.board[move-1] == ' '
  
  def board_is_full(self): #checks if the board is full
    for i in self.board:
      if i == ' ':
        return False
    return True
  
  def is_winner(self, player):
    piece = ""
    if player == 1:
      piece = "x"
    else:
      piece = "o"

    return ((self.board[6] == piece and self.board[7] == piece and self.board[8] == piece) or
    (self.board[3] == piece and self.board[4] == piece and self.board[5] == piece) or # across the middle
    (self.board[0] == piece and self.board[1] == piece and self.board[2] == piece) or # across the bottom
    (self.board[6] == piece and self.board[3] == piece and self.board[0] == piece) or # down the left side
    (self.board[7] == piece and self.board[4] == piece and self.board[1] == piece) or # down the middle
    (self.board[8] == piece and self.board[5] == piece and self.board[2] == piece) or # down the right side
    (self.board[6] == piece and self.board[4] == piece and self.board[2] == piece) or # diagonal
    (self.board[8] == piece and self.board[4] == piece and self.board[0] == piece)) # diagonal

  def switch_player(self, player):
    if player == 1:
      return 2
    else:
      return 1

# run the game
game = tic_tac_toe()
game.play()

