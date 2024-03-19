import random

def turn(pos1):
    diceroll = random.randint(1,6)
    if(diceroll == 6):
        print("6! extra roll")
        diceroll += random.randint(1,6)
    pos1 = pos1 + diceroll
    print("dice: ", diceroll)
    if(pos1 < 50): 
        #snakes
        if(pos1 == 8):
            pos1 == 4
            print("snake!")
            print("position: ", pos1)
        if(pos1 == 18):
            pos1 == 1
            print("snake!")
            print("position: ", pos1)
        if(pos1 == 26):
            pos1 == 10
            print("snake!")
            print("position: ", pos1)
        if(pos1 == 39):
            pos1 == 5
            print("snake!")
            print("position: ", pos1)
        if(pos1 == 49):
            pos1 == 2
            print("snake!")
            print("position: ", pos1)
        
        #ladders
        if(pos1 == 3):
            pos1 == 20
            print("ladder")
            print("position: ", pos1)
        if(pos1 == 6):
            pos1 == 14
            print("ladder")
            print("position: ", pos1)
        if(pos1 == 11):
            pos1 == 28
            print("ladder")
            print("position: ", pos1)
        if(pos1 == 15):
            pos1 == 34
            print("ladder")
            print("position: ", pos1)
        if(pos1 == 30):
            pos1 == 47
            print("ladder")
            print("position: ", pos1)
        print("position: ", pos1)
    elif(pos1 > 50):
        pos1 -= diceroll
        print("wait for next turn")
    return pos1

p1name = input("enter player 1 name: ")
p2name = input("enter player 2 name: ")
player1Pos = 40
player2Pos = 40
flag = 0
win = 0
while(player1Pos < 50 and player2Pos < 50):
    while(flag==0 and win==0):
        print("\n",p1name)
        a = input("enter 'roll' to start turn. ")
        if(a == "roll"):
            player1Pos = turn(player1Pos)
        if(player1Pos == 50):
            print("player 1 wins.")
            win = 1
        elif(player1Pos > 50):
            print("wait for turn")
        flag = 1
    while(flag==1 and win==0):
        print("\n",p2name)
        a = input("enter 'roll' to start turn. ")
        if(a == "roll"):
            player2Pos = turn(player2Pos)
        if(player2Pos == 50):
            print("player 2 wins.")
            win = 1
        elif(player2Pos > 50):
            print("wait for turn")
        flag = 0