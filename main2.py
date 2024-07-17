def printGrid(gridState):
    pipe_separated_rows = [' | '.join(map(str, row)) for row in gridState]
    global output
    output = '\n'.join(pipe_separated_rows)
    print(output)


def makeGrid(numRows, numColumns, gridState):

    numRows = int(input('Enter number of rows: '))
    numColumns = int(input('Enter number of columns: '))

    for i in range(numRows):
        gridState.append([])
        i += 1

    for row in gridState:
        for j in range(numColumns):
            row.append(' ')
            j += 1

    

    gridState[0][0] = '>'

    printGrid(gridState)

def newPosCalc(gridState, notInBounds, travelled, columnIndex, rowIndex, numRows, numColumns):
    # Ask person to input direction
        direction = input('Up (w), right (d), left (a) or down (s): ').lower()

        travelled = False
        notInBounds = False

        # Caculate new position
        if direction == 'w':
            if rowIndex - 1 < 0:
                print('Area out of bounds')
                notInBounds = True
            elif gridState[rowIndex - 1][columnIndex] == 'X':
                print('Already travelled here')
                travelled = True
            else:
                rowIndex -= 1
                symbol = '^'

        elif direction == 's':
            if rowIndex + 1 >= numRows:
                print('Area out of bounds')
                notInBounds = True
            elif gridState[rowIndex + 1][columnIndex] == 'X':
                print('Already travelled here')
                travelled = True
            else:
                rowIndex += 1
                symbol = '|'

        elif direction == 'a':
            if columnIndex - 1 < 0:
                print('Area out of bounds')
                notInBounds = True
            elif gridState[rowIndex][columnIndex - 1] == 'X':
                print('Already travelled here')
                travelled = True
            else:
                columnIndex -= 1
                symbol = '<'

        elif direction == 'd':
            if columnIndex + 1 >= numColumns:
                print('Area out of bounds')
                notInBounds = True
            elif gridState[rowIndex][columnIndex + 1] == 'X':
                print('Already travelled here')
                travelled = True
            else:
                columnIndex += 1
                symbol = '>'

def checkGridFull(gridState):
    gridFull = True
        
    for row in gridState:
        for item in row:
            if item == ' ':
                gridFull = False
                

    if gridFull == True:
        print('Grid is full')
        asking = False

def run():
    # Initialization
    symbol = ''
    numRows = 0
    numColumns = 0
    gridState = []

    makeGrid(numRows, numColumns, gridState)

    asking = True
    rowIndex = 0
    columnIndex = 0

    while asking:

        travelled = False
        notInBounds = False

        newPosCalc(gridState, notInBounds, travelled, columnIndex, rowIndex, numRows, numColumns)

        # Check if new position is in bounds

        newPos = gridState[rowIndex][columnIndex]

        # Check if path has already been travelled
        # Move to new position

        while travelled == True or notInBounds == True:
            newPosCalc(gridState, notInBounds, travelled, columnIndex, rowIndex, numRows, numColumns)

        gridState[rowIndex][columnIndex] = symbol

        # print grid
        printGrid(gridState)
        
        # Check if grid full

        checkGridFull(gridState)

run()