numberDictionary = {
    "0": " _\n| |\n|_|",
    "1": "  |\n  |",
    "2": " _\n _|\n|_",
    "3": " _\n _|\n _|\n",
    "4": "|_|\n  |",
    "5": " _\n|_\n _|",
    "6": " _\n|_\n|_|",
    "7": " _\n  |\n  |",
    "8": " _\n|_|\n|_|",
    "9": " _\n|_|\n _|"
}
mainMenuList = ['Show List', 'Add List', 'Sign Out']
listButton = ['To Main Menu']
theList = []


def showList():
    if theList == []:
        print('No Data')
    else:
        for x in theList:
            for k, v in numberDictionary.items():
                if str(x) == k:
                    print(f"{v}")
    
    for x, value in enumerate(listButton):
        print(f"{x}. {value}")
    pilihan = int(input("Input your choice: ")) 

    if pilihan == listButton.index('To Main Menu'):
        mainMenu()


def addList():
    addNumber = input("Add Number: ")
    theList.append(addNumber)
    mainMenu()


def mainMenu():
    for x, v in enumerate(mainMenuList):
        print(f"{x+1}. {v}")

    pilihan = int(input("Input your choice: "))

    if pilihan - 1 == mainMenuList.index('Show List'):
        showList()
    elif pilihan - 1 == mainMenuList.index('Add List'):
        addList()
    elif pilihan - 1 == mainMenuList.index('Sign Out'):
        return


if True:
    mainMenu()
