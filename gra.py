import random
import getpass
signs = ["p", "r", "s"]
myChoice = []
computerChoice = []
myScore = 0
computerScore = 0

while True:
    gameMode = input("Tryb gry: \n (P) 2graczy: \n (K) przeciwko komputerowi: ").upper()
    if(gameMode == "P"):
        rounds = int(input("Wybierz ilosc rund: "))
        player1 = input("Podaj nick")
        player2 = input("Podaj nick przeciwnika")
        for i in range(0,rounds):
            player = getpass.getpass(player1+" (r) rock, (p) paper, (s) scissors")
            bot = getpass.getpass(player2+" (r) rock, (p) paper, (s) scissors")
            myChoice.append(player)
            computerChoice.append(bot)
        for i in range(0,rounds):
            if (myChoice[i] == "p" and computerChoice[i] == "r") or (myChoice[i] == "r" and computerChoice[i] == "s") or (
                    myChoice[i] == "s" and computerChoice[i] == "p"):
                myScore = myScore + 1
            elif(myChoice[i] == "p" and computerChoice[i] == "p") or (myChoice[i] == "r" and computerChoice[i] == "r") or (
                    myChoice[i] == "s" and computerChoice[i] == "s"):
                    myScore+=1
                    computerScore+=1
            else:
                computerScore+=1

        if myScore>computerScore:
            print(player1+" wygrał!")
        elif myScore == computerScore:
            print("remis!")
        else:
            print(player2+" wygrał!")

        myChoice.clear()
        computerChoice.clear()
        myScore = 0
        computerScore = 0

    elif(gameMode == "K"):
        rounds = int(input("Wybierz ilosc rund: "))
        for i in range(0,rounds):
            player = input("(r) rock, (p) paper, (s) scissors")
            bot =signs[random.randint(0, len(signs)) - 1]
            myChoice.append(player)
            computerChoice.append(bot)
        for i in range(0,rounds):
            if (myChoice[i] == "p" and computerChoice[i] == "r") or (myChoice[i] == "r" and computerChoice[i] == "s") or (
                    myChoice[i] == "s" and computerChoice[i] == "p"):
                myScore = myScore + 1
            elif (myChoice[i] == "p" and computerChoice[i] == "p") or (myChoice[i] == "r" and computerChoice[i] == "r") or (
                    myChoice[i] == "s" and computerChoice[i] == "s"):
                myScore += 1
                computerScore += 1
            else:
                computerScore += 1

        if(myScore>computerScore):
            print("wygrales!")
        elif(myScore == computerScore):
            print("remis!")
        else:
            print("komputer wygral")
        myChoice.clear()
        computerChoice.clear()
        myScore = 0
        computerScore = 0

    elif(gameMode=="0"):
        break
    else:
        print("blad, wybierz poprawny tryb gry")