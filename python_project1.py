board=[i for i in range(10)]
print(board)

def display_board(board):
    print(  str(board[1]) + " | " + str(board[2]) + " | " + str(board[3]))
    print("--|--|--")
    print(  str(board[4]) + " | " + str(board[5]) + " | " + str(board[6]))
    print("--|--|--")
    print( str( board[7]) + " | " + str( board[8] )+ " | " + str(board[9]))
    print("--|--|--")
    print("\n")
    return "tic -tac -toe board"


res=display_board(board)

print(res)

player1="X"
player2="O"
playing=True
ch = 1
while playing:
    if ch%2 == 1:
        choice=int(input(f"player 1 please enter the position of board you want use ")) 
        if board[choice] != player1 and board[choice] != player2:
            board[choice]="X"
            display_board(board)
            ch+=1
        else :
            print("this place is not empty try again")
    elif ch%2 == 0:
        choice=int(input(f"player 2 please enter the position of board you want use ")) 
        if board[choice] != player1 and board[choice] != player2:
            board[choice]="O"
            display_board(board)
            ch+=1
        else :
            print("this place is not empty try again")

        if board[1]==board[2]==board[3]=='X' or board[4]==board[5]==board[6]=='X' or board[7]==board[8]==board[9]=='X' :
            print(f"Player one won ")
            break 
        elif board[1]==board[5]==board[9]=='X' or board[1]==board[4]==board[7]=='X' or  board[2]==board[5]==board[8]=='X' or board[3]==board[6]==board[9]=='X' :
            print(f"Player one won ")
            break 
        if board[1]==board[2]==board[3]=='O' or board[4]==board[5]==board[6]=='O' or board[7]==board[8]==board[9]=='O' :
            print(f"Player one won ")
            break 
        elif board[1]==board[5]==board[9]=='O' or board[1]==board[4]==board[7]=='O' or  board[2]==board[5]==board[8]=='O' or board[3]==board[6]==board[9]=='O' :
            print(f"Player Two won ")
            break 
        

playing= False 
