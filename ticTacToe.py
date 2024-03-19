def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])
def spotCheck(spot):
    if(spot<1 or spot>9):
        print("out of range(1,9)")
        return False
    elif(board[spot] != ' '):
        print("spot occupied")
        return False
    return True
def fullBoard():
    for i in range(1, len(board)+1):
        if(board[i]==' '):
            return False
            break
    return True
def winCheck(mark, board):
    #print("winCheck")
    return ((board[1] == mark and board[2]==mark and board[3]==mark) or
            (board[4] == mark and board[5]==mark and board[6]==mark) or
            (board[7] == mark and board[8]==mark and board[9]==mark) or
            (board[1] == mark and board[4]==mark and board[7]==mark) or
            (board[2] == mark and board[5]==mark and board[8]==mark) or
            (board[3] == mark and board[6]==mark and board[9]==mark) or
            (board[1] == mark and board[5]==mark and board[9]==mark) or
            (board[3] == mark and board[5]==mark and board[7]==mark))
    
board = {7: ' ', 8: ' ', 9: ' ',
         4: ' ', 5: ' ', 6: ' ',
         1: ' ', 2: ' ', 3: ' '}
p1name = input("enter player 1 name: ")
p2name = input("enter player 2 name: ")
drawBoard(board)
print("\n",p1name)
p1symbol = input("'x' or 'o': ")
p2symbol = ""
if p1symbol == 'x':
    p2symbol = 'o';
else:
    p2symbol = 'x';

flag=0
over=0
while(over==0):
    while(flag==0 and over==0):
        print("\n", p1name)
        x = int(input("enter spot: "))
        while(spotCheck(x)==False):
            x = int(input("enter spot: ")) 
            spotCheck(x)
        if(spotCheck(x)):
            board[x]='x'
        drawBoard(board)
        if(winCheck('x', board)):
            print(p1name, "wins!")
            over=1
        if(fullBoard()):
            print("draw!")
            over=1
        flag=1
    while(flag==1 and over==0):
        print("\n", p2name)
        o = int(input("enter spot: "))
        while(spotCheck(o)==False):
            o = int(input("enter spot: ")) 
            spotCheck(o)
        if(spotCheck(o)):
            board[o]='o'
        drawBoard(board)
        if(winCheck('o', board)):
            print(p2name, "wins!")
            over=1
        if(fullBoard()):
            print("draw!")
            over=1
        flag=0  