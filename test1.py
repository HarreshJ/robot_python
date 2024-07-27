car  = {
    'colour': 'blue',
    'model': 'Audi',
    'best feature': 'comfy seats'
}



def defineWord(dictionary):
    userInput = input("Enter word: ")
    if userInput in symbols:
        print(symbols[userInput])
    else:
        print('Word does not exist')

defineWord(symbols)