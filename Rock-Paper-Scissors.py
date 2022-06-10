## Nicholas Allen
## Rock, Paper, Scissors
## Submitted to DeVry 
import os
import random
gameChoice = ''
gameSymbols = ['Rock', 'Paper', 'Scissors']
symbolChoice = ''
symbol = ''

def main():
        ## Main function
    ## ╔╗╚╝═║╢─╟

    clearScreen()
    mainMenu()       
    #chooseSymbol()
    #print(gameChoice)
    #print(chooseSymbol)
    
def mainMenu():
    global gameChoice
    print('╔════════════════════════════════════╗\n'
          '║    ROCK - PAPER - SCISSORS GAME    ║\n'
          '╟────────────────────────────────────╢\n'
          '║      Please Choose Game Type       ║\n'
          '╟────────────────────────────────────╢\n'
          '║  1. Single game                    ║\n'
          '║  2. Best 2 out of 3 game           ║\n'
          '║  3. Best 3 out of 5 game           ║\n'
          '║  4. Choose number of games         ║\n'
          '╟────────────────────────────────────╢\n'
          '║  5. EXIT GAME                      ║\n'
          '╚════════════════════════════════════╝')
    gameChoice = input(': ')
    if gameChoice != "1" and gameChoice != "2" and gameChoice != "3" and gameChoice != "4" and gameChoice != "5":
        print('Choice not available, Please try again.')
        mainMenu()
    elif gameChoice == "5":
        exit()
    else:
        chooseSymbol()
    
def randomNum(numRange):
    print('randomNum')
    ## Randomization function

def chooseSymbol():
    ## Choose Symbol selection Function
    global gameSymbols
    global symbolChoice
    global gameChoice
    global symbol
    
    print('╔════════════════════════════════════╗\n'
          '║     Please choose your symbol      ║\n'
          '╟────────────────────────────────────╢\n'
          '║  1. Rock                           ║\n'
          '║  2. Paper                          ║\n'
          '║  3. Scissors                       ║\n'
          '╟────────────────────────────────────╢\n'
          '║  4. BACK                           ║\n'
          '╚════════════════════════════════════╝')

    symbolChoice = input(': ')
    #print(symbolChoice)
    if symbolChoice != "1" and symbolChoice != "2" and symbolChoice != "3" and symbolChoice != "4":
        print('Choice not available, Please try again.')
        chooseSymbol()
    elif symbolChoice == "4":
        clearScreen()
        mainMenu()
    else:
        symbol = gameSymbols[int(symbolChoice) - 1]
        bStr = '\u0020' * (15 - len(symbol))
        clearScreen()
        print('╔════════════════════════════════════╗\n'
              '║   Your symbol is : ' + symbol + bStr + ' ║\n'
              '╟────────────────────────────────────╢')
    gameType(gameChoice)
    
def gameType(gType):
    ## Game type selection function
    print('║    You are playing game type: ' + gType + '    ║\n'
          '╟────────────────────────────────────╢')

    
    if gType == '1':
        print('║          A single game of          ║\n' 
              '║       Rock, Paper, Scissors        ║\n'
              '╟────────────────────────────────────╢')
        playGame(1)
              #'║  Results:                          ║'
    if gType == '2':
        print('║          Best 2 out of 3           ║\n' 
              '║       Rock, Paper, Scissors        ║\n'
              '╟────────────────────────────────────╢')
        playGame(3)
    if gType == '3':
        print('║          Best 3 out of 5           ║\n' 
              '║       Rock, Paper, Scissors        ║\n'
              '╟────────────────────────────────────╢')
        playGame(5)
    if gType == '4':
        print('║ Run for specified number of games. ║\n' 
              '║     Games are aveaged together     ║\n'
              '║       to determine the winner      ║\n'
              '╟────────────────────────────────────╢')
        playGame(int(input('How many games?: ')))
                     

def playGame(gameNumber):
    global gameSymbols
    compWinCount = 0
    playerWinCount = 0
    tieCount = 0
    #GAME LOOP HERE
    #36 blanks - 12
    for i in range(gameNumber):
        bStr = '\u0020' * (25 - len(str(i)))
        print('║  Game #: ' + str(i + 1) + bStr + ' ║')
        computerChoice = random.choice(['Rock', 'Paper', 'Scissors'])
        bStr = '\u0020' * (23 - len(computerChoice))
        print('║  Computer: ' + computerChoice + bStr + ' ║')
        bStr = '\u0020' * (25 - len(symbol))
        print('║  Player: ' + symbol + bStr + ' ║')
            #print(computerChoice)
        if computerChoice == "Paper" and symbol == "Rock":
            print('║  Computer Wins!                    ║\n'
                  '╟────────────────────────────────────╢')
            compWinCount += 1
        elif computerChoice == "Rock" and symbol == "Scissors":
            print('║  Computer Wins!                    ║\n'
                  '╟────────────────────────────────────╢')
            compWinCount += 1
        elif computerChoice == "Scissors" and symbol == "Paper":
            print('║  Computer Wins!                    ║\n'
                  '╟────────────────────────────────────╢')
            compWinCount += 1
        elif computerChoice == "Paper" and symbol == "Paper":
            print('║  TIE!                              ║\n'
                  '╟────────────────────────────────────╢')
            tieCount += 1
        elif computerChoice == "Rock" and symbol == "Rock":
            print('║  TIE!                              ║\n'
                  '╟────────────────────────────────────╢')
            tieCount += 1
        elif computerChoice == "Scissors" and symbol == "Scissors":
            print('║  TIE!                              ║\n'
                  '╟────────────────────────────────────╢')
            tieCount += 1
        else:
            print('║  Player Wins!                      ║\n'
                  '╟────────────────────────────────────╢')
            playerWinCount += 1

#    bStr = '\u0020' * (16 - len(str(playerWinCount)))   
#    print('║  Player Won ' + str(playerWinCount) + ' Times ' + bStr + '║\n'
    bStr = '\u0020' * (14 - len(str(compWinCount)))   
    print('║  Computer Won ' + str(compWinCount) + ' Times ' + bStr + '║')
    bStr = '\u0020' * (16 - len(str(playerWinCount)))   
    print('║  Player Won ' + str(playerWinCount) + ' Times ' + bStr + '║')
    bStr = '\u0020' * (18 - len(str(tieCount)))   
    print('║  Number of Ties: ' + str(tieCount) + bStr + '║\n'
          '╚════════════════════════════════════╝')
    if input('Play again? (y/n) ').lower() == 'y':
        main()
    else:
        exit
def makeSelection():
    print('makeSelection')
    
def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    

if __name__ == "__main__":
    main()