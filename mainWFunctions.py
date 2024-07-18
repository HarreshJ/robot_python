class GameState:
    def __init__(self):
        self.travelled = False
        self.notInBounds = False
        self.rowIndex = 0
        self.columnIndex = 0
        self.numRows = int(input('Enter number of rows: '))
        self.numColumns = int(input('Enter number of columns: '))
        self.gridState = []
        self.asking = True

currentGameState = GameState()

def makeGrid():
    for i in range(currentGameState.numRows):
        currentGameState.gridState.append([])
        i += 1

    for row in currentGameState.gridState:
        for j in range(currentGameState.numColumns):
            row.append(' ')
            j += 1

    currentGameState.gridState[0][0] = '>'

def printGrid():
    gridState = currentGameState.gridState
    pipe_separated_rows = [' | '.join(map(str, row)) for row in gridState]
    output = '\n'.join(pipe_separated_rows)
    print(output)

def newPosCalc(symbol):
    direction = input('Up (w), right (d), left (a) or down (s): ').lower()

    if direction == 'w':
        if currentGameState.rowIndex - 1 < 0:
            print('Area out of bounds')
            currentGameState.notInBounds = True
            currentGameState.notInBounds = True
        elif currentGameState.gridState[currentGameState.rowIndex - 1][currentGameState.columnIndex] != ' ':
            print('Already travelled here')
            currentGameState.travelled = True
        else:
            currentGameState.rowIndex -= 1
            symbol = '^'

    elif direction == 's':
        if currentGameState.rowIndex + 1 >= currentGameState.numRows:
            print('Area out of bounds')
            currentGameState.notInBounds = True
        elif currentGameState.gridState[currentGameState.rowIndex + 1][currentGameState.columnIndex] != ' ':
            print('Already travelled here')
            currentGameState.travelled = True
        else:
            currentGameState.rowIndex += 1
            symbol = '/'

    elif direction == 'a':
        if currentGameState.columnIndex - 1 < 0:
            print('Area out of bounds')
            currentGameState.notInBounds = True
        elif currentGameState.gridState[currentGameState.rowIndex][currentGameState.columnIndex - 1] != ' ':
            print('Already travelled here')
            currentGameState.travelled = True
        else:
            currentGameState.columnIndex -= 1
            symbol = '<'

    elif direction == 'd':
        if currentGameState.columnIndex + 1 >= currentGameState.numColumns:
            print('Area out of bounds')
            currentGameState.notInBounds = True
        elif currentGameState.gridState[currentGameState.rowIndex][currentGameState.columnIndex + 1] != ' ':
            print('Already travelled here')
            currentGameState.travelled = True
        else:
            currentGameState.columnIndex += 1
            symbol = '>'

    else:
        print('Sorry, input not identified please try again later')
        currentGameState.asking = False

    currentGameState.gridState[currentGameState.rowIndex][currentGameState.columnIndex] = symbol
    newPos = currentGameState.gridState[currentGameState.rowIndex][currentGameState.columnIndex]

def newPosAfterCheck(symbol):
    direction = input('Up (w), right (d), left (a) or down (s): ').lower()

    if direction == 'w':
        if currentGameState.rowIndex - 1 < 0:
            print('Area out of bounds')
            currentGameState.notInBounds = True
        elif currentGameState.gridState[currentGameState.rowIndex - 1][currentGameState.columnIndex] != ' ':
            print('Already travelled here')
            currentGameState.travelled = True
        else:
            currentGameState.rowIndex -= 1
            symbol = '^'
            currentGameState.travelled = False
            currentGameState.notInBounds = False

    elif direction == 's':
        if currentGameState.rowIndex + 1 >= currentGameState.numRows:
            print('Area out of bounds')
            currentGameState.notInBounds = True
        elif currentGameState.gridState[currentGameState.rowIndex + 1][currentGameState.columnIndex] != ' ':
            print('Already travelled here')
            currentGameState.travelled = True
        else:
            currentGameState.rowIndex += 1
            currentGameState.travelled = False
            currentGameState.notInBounds = False
            symbol = '/'

    elif direction == 'a':
        if currentGameState.columnIndex - 1 < 0:
            print('Area out of bounds')
            currentGameState.notInBounds = True
        elif currentGameState.gridState[currentGameState.rowIndex][currentGameState.columnIndex - 1] != ' ':
            print('Already travelled here')
            currentGameState.travelled = True
        else:
            currentGameState.columnIndex -= 1
            currentGameState.travelled = False
            currentGameState.notInBounds = False
            symbol = '<'

    elif direction == 'd':
        if currentGameState.columnIndex + 1 >= currentGameState.numColumns:
            print('Area out of bounds')
            currentGameState.notInBounds = True
        elif currentGameState.gridState[currentGameState.rowIndex][currentGameState.columnIndex + 1] != ' ':
            print('Already travelled here')
            currentGameState.travelled = True
        else:
            currentGameState.columnIndex += 1
            currentGameState.travelled = False
            currentGameState.notInBounds = False
            symbol = '>'

    else:
        print('Sorry, input not identified please try again later')

    currentGameState.gridState[currentGameState.rowIndex][currentGameState.columnIndex] = symbol
    newPos = currentGameState.gridState[currentGameState.rowIndex][currentGameState.columnIndex]

def checkGridFull():
    gridFull = True
    currentGameState.gridState 
        
    for row in currentGameState.gridState:
        for item in row:
            if item == ' ':
                gridFull = False
                
    if gridFull == True:
        print('Grid is full')
        currentGameState.asking = False

def checkInBoundsandNotTravelled(symbol):

    while currentGameState.travelled == True or currentGameState.notInBounds == True:
            newPosAfterCheck(symbol)

def run():
    # Initialization
    numRows = 0
    numColumns = 0
    symbol = ''

    makeGrid()
    currentGameState.gridState[0][0] = '>'

    printGrid()

    while currentGameState.asking:

        currentGameState.gridState[0][0] = '>'

        symbol = ''
        # Ask person to input direction
        # Caculate new position

        newPosCalc(symbol)
        
        # Check if new position is in bounds
        # Check if path has already been travelled
        # Move to new position

        checkInBoundsandNotTravelled(symbol)

        # print grid
        printGrid()
        
        # Check if Grid is full
        checkGridFull()

run()