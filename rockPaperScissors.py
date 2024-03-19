import random
pScore = 0
cScore = 0
while(pScore < 3 and cScore < 3):   
    choices = ["rock", "paper", "scissors"]
    a = input("enter choice: ")
    b = random.choice(choices)
    print("computer's choice: ", b)
    if((a == "rock" and b == "scissors") or (a == "paper" and b == "rock") or (a == "scissors" and b == "paper")):
        print("you win!")
        pScore += 1
    elif((a == "rock" and b == "paper") or (a == "paper" and b == "scissors") or (a == "scissors" and b == "rock")):
        print("computer wins!")
        cScore += 1
    elif(a == b):
        print("tie!")
    print("")
    print("your score: ", pScore)
    print("computer's score: ", cScore)
    print("")
if(pScore > cScore):
    print("YOU WIN")
else:
    print("COMPUTER WINS")
#rockpapersiscors with list of choices best till 5
