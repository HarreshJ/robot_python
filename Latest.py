class GameState:
    def __init__(self):
        self.travelled = False
        self.notInBounds = False
        self.rowIndex = 0
        self.columnIndex = 0
        self.gridState = []
        self.asking = True

currentGameState = GameState()

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

def printGrid():
    pipe_separated_rows = [' | '.join(map(str, row)) for row in currentGameState.gridState]
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
    elif userInput == 'lru':
        return (currentPos[0] - 1, currentPos[1] + 1)
    elif userInput == 'lrd':
        return (currentPos[0] + 1, currentPos[1] + 1)
    elif userInput == 'llu':
        return (currentPos[0] - 1, currentPos[1] - 1)
    elif userInput == 'lld':
        return (currentPos[0] + 1, currentPos[1] - 1)          
        
    else:
        print('Input not valid try again later')

def nextSymbol(userInput, currentSymbol):
    if userInput == 'w':
        return '^'
    elif userInput == 's':
        return '|'
    elif userInput == 'a':
        return '<'
    elif userInput == 'd':
        return '>'
    elif userInput == 'j':
        return currentSymbol
    elif userInput == 'lru' or 'lrd' or 'llu' or 'lld':
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
    rowIndex = 0
    columnIndex = 0
    currentPos = rowIndex, columnIndex
    numRows = int(input('Number of rows: '))
    numColumns = int(input('Number of columns: '))
    currentGameState.gridState = makeGrid(numRows, numColumns)
    currentGameState.gridState[0][0] = '>'

    printGrid()

    print('UP = W \nLEFT = A \nDOWN = S \nRIGHT = D \nJUMP = J \nDIAGONAL = LRU or LRD or LLU or LLD \nNOTE: CANNOT JUMP IN DIAGONAL')

    
    while not gameOver:

        # Ask for input and check input validity

        direction = input('Enter your input here: ').lower() 
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
        nextPos = calculate_next_position(direction, currentPos, symbol)

        # Check if new position is in bounds
        isNotInBounds = notInBounds(numRows, numColumns, nextPos)
        if isNotInBounds:           
            print('Area not in bounds')
            continue
        
        # Check if path has already been travelled
        hasBeenTravelled = travelled(currentGameState.gridState, nextPos)
        if hasBeenTravelled:
            print('Path has already been travelled\n')
            print('Here is the grid before this move:')
            printGrid()
            continue

        # Move to new position
        symbol = nextSymbol(direction, symbol)
        move_to_next_pos(currentGameState.gridState, nextPos, symbol)

        #incrementing the current position so it moves along with the next move
        currentPos = nextPos
        
        # print grid
        printGrid()

        # Check if Grid is full
        gridFull = checkGridFull(currentGameState.gridState)
        if gridFull:
            print('Grid is full')
            gameOver = True

run()