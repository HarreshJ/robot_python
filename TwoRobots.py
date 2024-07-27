class GameStateRob1:
    def __init__(self):
        self.travelled = False
        self.notInBounds = False
        self.rowIndex = 0
        self.columnIndex = 0
        self.gridState = []
        self.asking = True

class GameStateRob2:
    def __init__(self):
        self.travelled = False
        self.notInBounds = False
        self.rowIndex = 0
        self.columnIndex = 0
        self.gridState = []
        self.asking = True

robotOne = GameStateRob1()
robotTwo = GameStateRob2()

directionToSymbol = {
    'w': '^',
    'a': '<',
    's': '|',
    'd': '>'
}

def makeGrid(numRows, numColumns):
    gridState = []

    for i in range(numRows):
        gridState.append([])
        i += 1

    for row in gridState:
        for j in range(numColumns):
            row.append(' ')
            j += 1

    return gridState

def printGrid(robotNum):
    pipe_separated_rows = [' | '.join(map(str, row)) for row in robotNum.gridState]
    output = '\n'.join(pipe_separated_rows)
    print(output)

def calculate_next_position(userInput, currentPos, theSymbol):
    if userInput == 'w':
        return (currentPos[0] - 1, currentPos[1])
    elif userInput == 's':
        return (currentPos[0] + 1, currentPos[1])
    elif userInput == 'a':
        return (currentPos[0], currentPos[1] - 1)
    elif userInput == 'd':
        return (currentPos[0], currentPos[1] + 1)
    elif userInput == 'j':
        if theSymbol == '^':
            return (currentPos[0] - 2, currentPos[1])
        elif theSymbol == '|':
            return (currentPos[0] + 2, currentPos[1])
        elif theSymbol == '<':
            return (currentPos[0], currentPos[1] - 2)
        elif theSymbol == '>':
            return (currentPos[0], currentPos[1] + 2)
    elif userInput == ('lru' or 'lru2'):
        return (currentPos[0] - 1, currentPos[1] + 1)
    elif userInput == ('lrd' or 'lrd2'):
        return (currentPos[0] + 1, currentPos[1] + 1)
    elif userInput == ('llu' or 'llu2'):
        return (currentPos[0] - 1, currentPos[1] - 1)
    elif userInput == ('lld' or 'lld2'):
        return (currentPos[0] + 1, currentPos[1] - 1)          
        
    else:
        print('Input not valid try again later')

def nextSymbol(userInput, currentSymbol, diagonals):
    if userInput in directionToSymbol:
       return directionToSymbol[userInput]
    elif userInput == 'j':
        return currentSymbol
    elif userInput in diagonals:
        return '/'
   
def notInBounds(numRows, numColumns, newPos):
    if (newPos[0] < 0) or (newPos[0] >= numRows) or (newPos[1] < 0) or (newPos[1] >= numColumns):
        return True
    else:
        return False

def travelled(gridState, newPos):
    if gridState[newPos[0]][newPos[1]] != ' ':    
        return True
    else:
        return False
    
def move_to_next_pos(gridState, newPos, theSymbol):
    gridState[newPos[0]][newPos[1]] = theSymbol

def checkGridFull(gridState):

    for row in gridState:
        for item in row:
            if item == ' ':
                return False
    else:
        return True

def run():
    # Initialization
    symbol = '>'
    gameOver = False
    rowIndex1 = 0
    columnIndex1 = 0
    currentPos1 = rowIndex1, columnIndex1
    rowIndex2 = 0
    columnIndex2 = 0
    currentPos2 = rowIndex2, columnIndex2

    numRows1 = int(input('Number of rows for Grid 1: '))
    numColumns1 = int(input('Number of columns for Grid 1: '))
    numRows2 = int(input('Number of rows for Grid 2: '))
    numColumns2 = int(input('Number of columns for Grid 2: '))


    robotOne.gridState = makeGrid(numRows1, numColumns1)
    robotTwo.gridState = makeGrid(numRows2, numColumns2)
    robotOne.gridState[0][0] = '>'
    robotTwo.gridState[0][0] = '>'
    playerTurn = 1
    gridFull1 = False
    gridFull2 = False
    diagonals = ['lru', 'lrd', 'llu', 'lld']

    print('UP = W \nLEFT = A \nDOWN = S \nRIGHT = D \nJUMP = J \nDIAGONAL = LRU or LRD or LLU or LLD')
    
    while not gameOver:
        if playerTurn == 1:
            print('Robot 1: ')
            printGrid(robotOne)
    
        else:
            print('Robot 2: ')
            printGrid(robotTwo)

        # Ask for input and check input validity

        direction = input('Enter your input here for robot' + str(playerTurn) + ': ').lower() 
        validMoves = ['w', 'a', 's', 'd', 'j', 'lru', 'lrd', 'llu', 'lld']
        invalidInput = False

        if direction not in validMoves:
            print('INPUT NOT VALID')
            invalidInput = True

            while invalidInput:
                direction = input('Enter your input here: ').lower()

                if direction in validMoves:
                    invalidInput = False 

                else:
                    print('Input still invalid')

        # Caculate new position
        # Check if new position is in bounds
        # Check if path has already been travelled

        if playerTurn == 1:
            nextPos1 = calculate_next_position(direction, currentPos1, symbol)
            isNotInBounds = notInBounds(numRows1, numColumns1, nextPos1)
            hasBeenTravelled = travelled(robotOne.gridState, nextPos1)
        else:
            nextPos2 = calculate_next_position(direction, currentPos2, symbol)
            isNotInBounds = notInBounds(numRows2, numColumns2, nextPos2)
            hasBeenTravelled = travelled(robotTwo.gridState, nextPos2)
        
        if isNotInBounds:           
            print('Area not in bounds')
            continue
        
        if hasBeenTravelled:
            print('Path has already been travelled\n')
            print('Here is the grid before this move:')
            if playerTurn == 1:
                print('Robot 1: ')
                printGrid(robotOne)
            else:
                print('Robot 2: ')
                printGrid(robotTwo)
            continue

        # Move to new position
        #incrementing the current position so it moves along with the next move
        # print grid
        # Check if Grid is full

        symbol = nextSymbol(direction, symbol, diagonals)
        if playerTurn == 1:
            move_to_next_pos(robotOne.gridState, nextPos1, symbol)
            currentPos1 = nextPos1
            print('Robot 1: ')
            printGrid(robotOne)
            gridFull1 = checkGridFull(robotOne.gridState)
        else:
            move_to_next_pos(robotTwo.gridState, nextPos2, symbol)
            currentPos2 = nextPos2
            print('Robot 2: ')
            printGrid(robotTwo)
            gridFull2 = checkGridFull(robotTwo.gridState)    

        if gridFull1 or gridFull2:
            print('Grid is full')

        # Player swap
        if gridFull1 or gridFull2:
            if gridFull1 and gridFull2:
                gameOver = True
            elif gridFull1:
                playerTurn = 2
                continue
            elif gridFull2:
                playerTurn = 1
                continue
        
        else:
            if playerTurn == 1:
                playerTurn = 2
            else:
                playerTurn = 1

run()