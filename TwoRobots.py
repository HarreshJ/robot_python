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

def nextSymbol(userInput, currentSymbol):
    diagonals = ['lru', 'lru2', 'lrd', 'lrd2', 'llu', 'llu2', 'lld', 'lld2']
    if userInput == 'w' or 'w2':
        return '^'
    elif userInput == 's' or 's2':
        return '|'
    elif userInput == 'a' or 'a2':
        return '<'
    elif userInput == 'd' or 'd2':
        return '>'
    elif userInput == 'j' or 'j2':
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
    numRows1 = int(input('Number of rows: '))
    numColumns1 = int(input('Number of columns: '))
    numRows2 = int(input('Number of rows: '))
    numColumns2 = int(input('Number of columns: '))
    robotOne.gridState = makeGrid(numRows1, numColumns1)
    robotTwo.gridState = makeGrid(numRows2, numColumns2)
    robotOne.gridState[0][0] = '>'
    robotTwo.gridState[0][0] = '>'

    printGrid(robotOne)
    printGrid(robotTwo)


    print('UP = W \nLEFT = A \nDOWN = S \nRIGHT = D \nJUMP = J \nDIAGONAL = LRU or LRD or LLU or LLD \nNOTE: CANNOT JUMP IN DIAGONAL \nAdd a 2 at the end of the input for the second robot')

    
    while not gameOver:

        # Ask for input and check input validity

        direction = input('Enter your input here: ').lower() 
        validMoves = ['w', 'a', 's', 'd', 'j', 'lru', 'lrd', 'llu', 'lld', 'w2', 'a2', 's2', 'd2', 'j2', 'lru2', 'lrd2', 'llu2', 'lld2']
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
        nextPos1 = calculate_next_position(direction, currentPos1, symbol)
        nextPos2 = calculate_next_position(direction, currentPos2, symbol)

        # Check if new position is in bounds
        isNotInBounds = notInBounds(numRows1, numColumns1, nextPos1)
        isNotInBounds = notInBounds(numRows2, numColumns2, nextPos2)
        if isNotInBounds:           
            print('Area not in bounds')
            continue
        
        # Check if path has already been travelled
        hasBeenTravelled = travelled(robotOne.gridState, nextPos1)
        hasBeenTravelled = travelled(robotTwo.gridState, nextPos2)
        if hasBeenTravelled:
            print('Path has already been travelled\n')
            print('Here is the grid before this move:')
            printGrid(robotOne)
            printGrid(robotTwo)
            continue

        # Move to new position
        symbol = nextSymbol(direction, symbol)
        move_to_next_pos(robotOne.gridState, nextPos1, symbol)
        move_to_next_pos(robotTwo.gridState, nextPos2, symbol)

        #incrementing the current position so it moves along with the next move
        currentPos1 = nextPos1
        currentPos2 = nextPos2
                
        # print grid
        printGrid(robotOne)
        printGrid(robotTwo)

        # Check if Grid is full
        gridFull = checkGridFull(robotOne.gridState)
        gridFull = checkGridFull(robotTwo.gridState)

        if gridFull:
            print('Grid is full')
            gameOver = True

run()