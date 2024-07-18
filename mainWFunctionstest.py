class GameState:
    def __init__(self):
        self.travelled = False
        self.notInBounds = False
        self.rowIndex = 0
        self.columnIndex = 0
        self.gridState = []
        self.asking = True

class Pos:
    def __init__(self, rowIndex, columnIndex):
        self.rowIndex = rowIndex
        self.columnIndex = columnIndex

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

def calculate_next_position(userInput, currentPos):
    if userInput == 'w':
        return Pos(currentPos.rowIndex - 1, currentPos.columnIndex)
    elif userInput == 's':
        return Pos(currentPos.rowIndex + 1, currentPos.columnIndex)
    elif userInput == 'a':
        return Pos(currentPos.rowIndex, currentPos.columnIndex - 1)
    elif userInput == 'd':
        return Pos(currentPos.rowIndex, currentPos.columnIndex + 1)
    else:
        print('Input not valid try again later')

def nextSymbol(userInput):
    if userInput == 'w':
        symbol = '^'
    elif userInput == 's':
        symbol = '/'
    elif userInput == 'a':
        symbol = '<'
    elif userInput == 'd':
        symbol = '>'

    return symbol

def notInBounds(numRows, numColumns, newPos):
    if (newPos.rowIndex < 0) or (newPos.rowIndex >= numRows) or (newPos.columnIndex < 0) or (newPos.columnIndex >= numColumns):
        return True
    else:
        return False

def travelled(gridState, newPos):
    if gridState[newPos.rowIndex][newPos.columnIndex] != ' ':    
        return True
    else:
        return False
    
def move_to_next_pos(gridState, newPos, theSymbol):
    gridState[newPos.rowIndex][newPos.columnIndex] = theSymbol

def checkGridFull(gridState):

    for row in gridState:
        for item in row:
            if item == ' ':
                return False
    else:
        return True

def run():
    # Initialization
    symbol = ''
    gameOver = False
    currentPos = Pos(0,0)
    numRows = int(input('Number of rows: '))
    numColumns = int(input('Number of columns: '))

    currentGameState.gridState = makeGrid(numRows, numColumns)
    currentGameState.gridState[0][0] = '>'

    printGrid()

    while not gameOver:

        # Ask person to input direction
        direction = input('Up (w), right (d), left (a) or down (s): ').lower() 

        # Caculate new position
        nextPos = calculate_next_position(direction, currentPos)

        # Check if new position is in bounds
        isNotInBounds = notInBounds(numRows, numColumns, nextPos)
        if isNotInBounds:           
            print('Area not in bounds')
            continue
        
        # Check if path has already been travelled
        hasBeenTravelled = travelled(currentGameState.gridState, nextPos)
        if hasBeenTravelled:
            print('Path has already been travelled')
            continue

        # Move to new position
        symbol = nextSymbol(direction)
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