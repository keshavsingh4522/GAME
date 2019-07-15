def tic_tac_toe():
 board=[1,2,3,4,5,6,7,8,9]
 end=False
 win_combinations=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

 def draw():
  print('--------------------')
  print('| ',board[0],' | ',board[1],' | ',board[2],' | ')
  print('| ',board[3],' | ',board[4],' | ',board[5],' | ')
  print('| ',board[6],' | ',board[7],' | ',board[8],' | ')
  print('--------------------')

 def p1():
  print("player p1 -> choose your place to place 'X' : ",end='')
  n=int(input())
  if board[n-1]=='X' or board[n-1]=='O':
   print("!you can't place 'X' choose other place")
   p1()
  else:
   board[n-1]='X';

 def p2():
  print("player p2 -> choose your place to place 'O': ",end='')
  n=int(input())
  if board[n-1]=='X' or board[n-1]=='O':
   print("!you can't place 'O' choose other place")
   p2()
  else:
   board[n-1]='O';

 def check_board():
  for a in win_combinations:
   if board[a[0]]==board[a[1]]==board[a[2]]=='X':
    print('\nCongratulations!!\nPlayer P1 wins!!')
    return True
   if board[a[0]]==board[a[1]]==board[a[2]]=='O':
    print('\nCongratulations!!\nPlayer P2 wins!!')
    return True
  count=0
  for a in range(9):
   if board[a]=='X' or board[a]=='O':
    count+=1
   if count==9:
    return True
  return False

 while not end:
  draw()
  p1()
  draw()
  end=check_board()
  if end==True:
   break

  p2()
  draw()
  end=check_board()
  if end==True:
   break
 yn=input('\nare you want to play again?(y/n)')
 if yn=='y' or yn=='Y':
  tic_tac_toe()
tic_tac_toe()
'''
output:
--------------------
|  1  |  2  |  3  | 
|  4  |  5  |  6  | 
|  7  |  8  |  9  | 
--------------------
player p1 -> choose your place to place 'X' : 1
--------------------
|  X  |  2  |  3  | 
|  4  |  5  |  6  | 
|  7  |  8  |  9  | 
--------------------
player p2 -> choose your place to place 'O': 4
--------------------
|  X  |  2  |  3  | 
|  O  |  5  |  6  | 
|  7  |  8  |  9  | 
--------------------
--------------------
|  X  |  2  |  3  | 
|  O  |  5  |  6  | 
|  7  |  8  |  9  | 
--------------------
player p1 -> choose your place to place 'X' : 5
--------------------
|  X  |  2  |  3  | 
|  O  |  X  |  6  | 
|  7  |  8  |  9  | 
--------------------
player p2 -> choose your place to place 'O': 7
--------------------
|  X  |  2  |  3  | 
|  O  |  X  |  6  | 
|  O  |  8  |  9  | 
--------------------
--------------------
|  X  |  2  |  3  | 
|  O  |  X  |  6  | 
|  O  |  8  |  9  | 
--------------------
player p1 -> choose your place to place 'X' : 9
--------------------
|  X  |  2  |  3  | 
|  O  |  X  |  6  | 
|  O  |  8  |  X  | 
--------------------

Congratulations!!
Player P1 wins!!

are you want to play again?(y/n)y
--------------------
|  1  |  2  |  3  | 
|  4  |  5  |  6  | 
|  7  |  8  |  9  | 
--------------------
player p1 -> choose your place to place 'X' : 1
--------------------
|  X  |  2  |  3  | 
|  4  |  5  |  6  | 
|  7  |  8  |  9  | 
--------------------
player p2 -> choose your place to place 'O': 6
--------------------
|  X  |  2  |  3  | 
|  4  |  5  |  O  | 
|  7  |  8  |  9  | 
--------------------
--------------------
|  X  |  2  |  3  | 
|  4  |  5  |  O  | 
|  7  |  8  |  9  | 
--------------------
player p1 -> choose your place to place 'X' : 4
--------------------
|  X  |  2  |  3  | 
|  X  |  5  |  O  | 
|  7  |  8  |  9  | 
--------------------
player p2 -> choose your place to place 'O': 3
--------------------
|  X  |  2  |  O  | 
|  X  |  5  |  O  | 
|  7  |  8  |  9  | 
--------------------
--------------------
|  X  |  2  |  O  | 
|  X  |  5  |  O  | 
|  7  |  8  |  9  | 
--------------------
player p1 -> choose your place to place 'X' : 7
--------------------
|  X  |  2  |  O  | 
|  X  |  5  |  O  | 
|  X  |  8  |  9  | 
--------------------

Congratulations!!
Player P1 wins!!

are you want to play again?(y/n)n
'''
