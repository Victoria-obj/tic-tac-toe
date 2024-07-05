import random
def display(row1, row2, row3):
   print("Current Board: ")
   print(row1)
   print(row2)
   print(row3)
def player_input():
    var_option = input("Player 1, choose X or O: ").upper()
    while var_option not in ['X', 'O']:
        print("Invalid choice!")
        var_option = input("Choose either X or O: ").upper()
    
    if var_option == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
   
def update_board(row1, row2, row3, var_option, row_option, index_option):
    if row_option == 1:
      row1[index_option - 1] = var_option
    elif row_option == 2:
      row2[index_option - 1] = var_option
    elif row_option == 3:
      row3[index_option - 1] = var_option
    return row1,row2,row3

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'player1'
    else:
        return 'player2'


def win_check(row1, row2, row3, var_option):
   #checking rows
    if [var_option]*3 in [row1, row2, row3]:
       print(f"player {var_option} WON!")
       return True
    #checking columns
    for col in range(3):
       if (row1[col] == row2[col] == row3[col] == var_option):
          print(f"player {var_option} WON!")
          return True

    #checking for diagonals
    if (row1[0]==row2[1]==row2[2]==var_option) or (row1[2]==row2[1]==row3[0]==var_option):
       print(f"player {var_option} WON!")
       return True

def board_full(row1, row2, row3):
    for row in [row1, row2, row3]:
        if '__' in row:
            return False
    return True
          
def play_again(): 
   choice = input("do you want to play again? YES or NO:  ").upper()
   return choice.upper() == 'YES'
   
print("TIC TAC TOE")
   
while True:
   row1 = ['__','__','__']
   row2 = ['__','__','__']
   row3 = ['__','__','__']    
   
   
   turn = choose_first()
   print(f"{turn}'s turn")

   play_game = input("are you ready to play? Y or N:  ").upper()
   if play_game == 'Y':
      game_on = True
   else:
      game_on = False


   while game_on:
        display(row1, row2, row3)
        var_option, opposite_option = player_input()
        row_option = int(input("Select a row (1, 2, 3): "))
        index_option = int(input("Select an index (1, 2, 3): "))

        if row_option not in [1, 2, 3] or index_option not in [1, 2, 3]:
            print("Invalid row or index option! Try again.")
            continue
           
        if turn == 'player1':
            row1, row2, row3 = update_board(row1, row2, row3, var_option, row_option, index_option)
            if win_check(row1, row2, row3, var_option):
                print(f"Player1 has won!")
                game_on = False
            elif board_full(row1, row2, row3):
                print("It's a tie!")
                game_on = False
            else:
                turn = 'player2'
                
        else:
            row1, row2, row3 = update_board(row1, row2, row3, opposite_option, row_option, index_option)
            if win_check(row1, row2, row3, opposite_option):
               print("player2 has won!")
               game_on = False
            elif board_full(row1, row2, row3):
               print("it's a tie")
               game_on = False
            else:
               turn = 'player1'
   
   
   if not play_again():
      break
