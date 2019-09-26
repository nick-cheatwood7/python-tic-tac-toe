import random

def drawBoard(boardList):
    print(' '+boardList[0]+' | '+boardList[1] + ' | ' + boardList[2])
    print('-----------')
    print(' '+boardList[3]+' | '+boardList[4] + ' | ' + boardList[5])
    print('-----------')
    print(' '+boardList[6]+' | '+boardList[7] + ' | ' + boardList[8])

    print('\n')


def isAvailable(boardList, move):
    if boardList[int(move)-1] != 'X' and \
    boardList[int(move)-1] != 'O':
        return True
    else:
        return False

def getThreeInRow(boardList):

    b = boardList
    # i = 0

    m = 0


    if (b[1] == 'O' and b[2] == 'O') or (b[4] == 'O' and b[8] == 'O') or (b[3] == 'O' and b[6] == 'O'):
        m = 1

    elif (b[0] == 'O' and b[2] == 'O') or (b[4] == 'O' and b[7] == 'O'):
        m = 2

    elif (b[1] == 'O' and b[0] == 'O') or (b[4] == 'O' and b[6] == 'O') or (b[5] == 'O' and b[8] == 'O'):
        m = 3

    elif (b[0] == 'O' and b[6] == 'O') or (b[4] == 'O' and b[5] == 'O'):
        m = 4

    elif (b[0] == 'O' and b[8] == 'O') or (b[1] == 'O' and b[7] == 'O') or (b[2] == 'O' and b[6] == 'O') or (b[3] == 'O' and b[5] == 'O'):
        m = 5

    elif (b[3] == 'O' and b[5] == 'O') or (b[2] == 'O' and b[8] == 'O'):
        m = 6

    elif (b[4] == 'O' and b[2] == 'O') or (b[0] == 'O' and b[3] == 'O') or (b[7] == 'O' and b[8] == 'O'):
        m = 7

    elif (b[1] == 'O' and b[4] == 'O') or (b[6] == 'O' and b[8] == 'O'):
        m = 8

    elif (b[0] == 'O' and b[4] == 'O') or (b[2] == 'O' and b[5] == 'O') or (b[6] == 'O' and b[7] == 'O'):
        m = 9

    else:
        m = 0

    # print('board:', b)
        # print(i)
        # i += 1
    return m



def getWinningCombo(boardList):

    # abbreviate the board list and create a new list to store the possible values for moves to take based off what spots are occupied
    # i might want to create an additional function to look for places where we could connect three in a row
    b = boardList
    l = []

    if b[0] == 'O': # 1
        l = [2,4,7,5,9] # combos with 1
    elif b[1] == 'O': # 2
        l = [1,3,5,8]
    elif b[2] == 'O': # 3
        l = [1,2,7,5,6,9]
    elif b[3] == 'O': # 4
        l = [1,5,6,7]
    elif b[4] == 'O': # 5
        l = [1,9,8,2,3,7,4,6]
    elif b[5] == 'O': # 6
        l = [3,9,4,5]
    elif b[6] == 'O': # 7
        l = [1,4,3,5,8,9]
    elif b[7] == 'O': # 8
        l = [2,5,7,9]
    elif b[8] == 'O': # 9
        l = [1,5,3,6,7,8]

    # print(l)

    r = random.choice(l)
    while not isAvailable(boardList, r):
        r = random.choice(l)

    return r


def computerMove(boardList):

    # print('Board', boardList)
    m = 0

    for v in boardList:
        if v == 'O':
            if getThreeInRow(boardList) != 0:
                #print('Three in row:', getThreeInRow(boardList))
                if isAvailable(boardList, getThreeInRow(boardList)):
                    return getThreeInRow(boardList)
                else:
                    m = getWinningCombo(boardList)
                    while not isAvailable(boardList, getWinningCombo(boardList)):
                        m = getWinningCombo(boardList)
                    return m
            else:
                #print('List:', getWinningCombo(boardList))
                m = getWinningCombo(boardList)
                while not isAvailable(boardList, getWinningCombo(boardList)):
                        m = getWinningCombo(boardList)
                return m
    else:
        return random.randint(1,9)




def getPlayerMove(boardList):
    playerMove = input('Enter number of move: ')
    while not isAvailable(boardList,playerMove):
        playerMove = input('Enter number of move: ')
    return playerMove

def isFull(boardList):
    for i in range(9):
        if boardList[i] == str(i+1):
            return False
    return True

def determineWinner(boardList):
    winner = '?'
    if boardList[0] == boardList[3] and boardList[3] == boardList[6]:
        winner = boardList[0]
    elif boardList[1] == boardList[4] and boardList[4] == boardList[7]:
        winner = boardList[1]
    elif boardList[2] == boardList[5] and boardList[5] == boardList[8]:
        winner = boardList[2]
    elif boardList[0] == boardList[1] and boardList[1] == boardList[2]:
        winner = boardList[0]
    elif boardList[3] == boardList[4] and boardList[4] == boardList[5]:
        winner = boardList[3]
    elif boardList[6] == boardList[7] and boardList[7] == boardList[8]:
        winner = boardList[6]
    elif boardList[0] == boardList[4] and boardList[4] == boardList[8]:
        winner = boardList[0]
    elif boardList[2] == boardList[4] and boardList[4] == boardList[6]:
        winner = boardList[2]
    else:
        winner = '?'
    return winner

def cls():
    print('\n' * 50)

def main():

    con = bool

    compScore = 0
    playerScore = 0

    while con != False:

        random.seed()
        board = ['1','2','3','4','5','6','7','8','9']
        drawBoard(board)
        #Player chooses piece
        # playerPiece = input('Do you want to be X or O? ').upper()
        playerPiece = 'X'

        if playerPiece != 'X' and playerPiece != 'O':
            print('Error. Must be an X or an O.')
            break

        #Determine computer piece
        if playerPiece == 'X':
            computerPiece = 'O'
        else:
            computerPiece = 'X'

        #Flip coin...who goes first
        playerFirst = True
        coin = random.randint(1,2) #let heads == 1
        # don't ask the user to choose heads or tails anymore
        # userChoice = input('Heads or tails? ')
        if (coin == 1):
            print('You go first!')
            print('\n')
        else:
            print('Computer goes first.')
            print('\n')
            playerFirst = False

        #Get moves
        if playerFirst:
            while not isFull(board) and determineWinner(board) == '?':
                playerMove = getPlayerMove(board)
                board[int(playerMove)-1] = playerPiece
                #drawBoard(board) - too much info on screen
                #Computer goes only if spot is available
                if not isFull(board) and determineWinner(board) == '?':
                    compMove = computerMove(board)
                    # print('Comp move:',compMove)

                    board[int(compMove)-1] = computerPiece
                drawBoard(board)
        else: #Computer first
            while not isFull(board) and determineWinner(board) == '?':

                compMove = computerMove(board)
                # print('Comp move:',compMove)


                board[int(compMove)-1] = computerPiece
                drawBoard(board)
                #Player goes only if spot is available
                if not isFull(board) and determineWinner(board) == '?':
                    playerMove = getPlayerMove(board)
                    board[int(playerMove)-1] = playerPiece
                #drawBoard(board)

        whoWon = determineWinner(board)

        if whoWon == playerPiece:
            print('Congratulations! You won!')
            print('\n')
            playerScore += 1
            print('Player: ', playerScore , '\n' + 'Computer: ', compScore)
            print('\n')

        elif whoWon == computerPiece:
            print('Better luck next time!')
            print('\n')
            compScore += 1
            print('Player: ', playerScore , '\n' + 'Computer: ', compScore)
            print('\n')

        else:
            print('Tie! Try again!')
            print('\n')


        userContinue = input('Continue (Y/N)? ').upper()
        if userContinue == 'Y':
            con = True
            cls()
        else:
            con = False

main()





