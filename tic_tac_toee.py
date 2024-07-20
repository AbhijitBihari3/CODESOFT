import random
board= [' ' for _ in range(9)]
def letter_insert(letter,pos):#function
    board[pos] = letter
def empty_space(pos):
    return board[pos]==' '
def printboard(board):
    print(' ' + board[0]+'|'+board[1]+'|'+board[2])
   
    print(' ' + board[3]+'|'+board[4]+'|'+board[5])
    
    print(' ' + board[6]+'|'+board[7]+'|'+board[8])
    print("_+_+_+_+")
def iswinner(bo,le):
    return((bo[0]==le and bo[1]==le and bo[2]==le) or
    (bo[3]==le and bo[4]==le and bo[5]==le) or
    (bo[6]==le and bo[7]==le and bo[8]==le) or
    (bo[0]==le and bo[3]==le and bo[6]==le)or
    (bo[1]==le and bo[4]==le and bo[7]==le)or
    (bo[2]==le and bo[5]==le and bo[8]==le)or
    (bo[0]==le and bo[4]==le and bo[8]==le)or
    (bo[2]==le and bo[4]==le and bo[6]==le))

def ai_move():
    possible_moves=[i for i,x in enumerate(board) if x==' ']
    move=random.choice(possible_moves)
    letter_insert('0',move)
    return
def player_turn():
    run = True
    while run:
        move=input("Select a pos(1-9) to place 'x': ")
        try:
            move=int(move)
            if move>0 and move<10:
                if empty_space(move-1):
                    run=False
                    letter_insert('x',move-1)
                else:
                    print('space is already filled')
            else:
                 print('invalid move')
        except:
            print("type a number")

def play_game():
    printboard(board)
    while True:
      player_turn()
      printboard(board)
      if iswinner(board,'x'):
       print("you win!! ^_^")
       break
      elif ' ' not in board:
       print("it's a tie -_-")
       break
      ai_move()
      printboard (board)
      if iswinner(board,'0'):
       print("ai wins :)")
       break
      elif ' ' not in board:
       print("it's a tie -_-")
       break
play_game()