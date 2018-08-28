listMainMenu = ['Lihat Semua Directory', 'Tambah Directory', 'Filter Directory', 'Hapus Directory', 'Keluar']
listTombol = ['0. Kembali ke Main Menu']
listTombolSearchMenu = ['Ke Menu Search', 'Kembali ke Main Menu']
listDirectory = {}
searchDictionary = {}

# Show All Directory
def allDirectory():
    if listDirectory == {}:
        print("No Data\n\n")
    else:
        print(f"key -> value\n")
        for x, value in listDirectory.items():
            if type(value) is str:
                print(f"{x} -> '{value}'")
            else:
                print(f"{x} -> {value}")
    print("\n\n")
    for x in listTombol:
        print(x)
    pilihan = int(input("Masukkan Pilihan: "))
    
    if pilihan == listTombol.index('0. Kembali ke Main Menu'):
        mainMenu()

# Delete Page Dictionary
def deleteDirectory():
    print(f"Key -> Values\n")
    for k, values in listDirectory.items():
        if type(values) is str:
            print(f"{k} -> '{values}'")
        else:
            print(f"{k} -> {values}")

    inputDel = input("Delete by Keys: ")
    listDirectory.pop(inputDel)
    mainMenu()

# Create new Directory
def newDirectory():
    listTypeValue = ['String', 'Integer']
    userInputKey = input("Masukkan Key: ")
    for i, x in enumerate(listTypeValue):
        print(f"{i+1}. {x}")
    userChoiceValue = input("Pilih Type value: ")
    userInputValue = input("Masukkan Value: ")

    if int(userChoiceValue)-1 == listTypeValue.index('String'):
        listDirectory[userInputKey] = userInputValue
    elif int(userChoiceValue)-1 == listTypeValue.index('Integer'):
        listDirectory[userInputKey] = int(userInputValue)
    mainMenu()

#Sub Filter Directory for search
def subFilterDirectory():
    if listDirectory == {}:
        print("No Data")
    else:
        print(listDirectory)
        inputSearch = input("Search: ")
        searchDictionary = dict(filter(lambda item: inputSearch.lower() in item[0].lower(), listDirectory.items()))
        print(f"key -> value\n")
        for x, value in searchDictionary.items():
            if type(value) is str:
                print(f"{x} -> '{value}'")
            else:
                print(f"{x} -> {value}")

        mainFilterDirectory()

# Main Filter Directory
def mainFilterDirectory():
    print("\n\nWelcome to Search Page\n\n")
    for x, value in enumerate(listTombolSearchMenu):
        print(f"{x+1}. {value}")
    pilihan = int(input("Masukkan Pilihan: "))
    if pilihan-1 == listTombolSearchMenu.index('Ke Menu Search'):
        subFilterDirectory()
    elif pilihan-1 == listTombolSearchMenu.index('Kembali ke Main Menu'):
        mainMenu()

# Main Menu
def mainMenu(): 
    print("<----Main Menu---->\n")
    for x, value in enumerate(listMainMenu):
        print(f"{x+1}. {value}")
    pilihan = int(input("Masukkan Pilihan: "))
    if (pilihan-1 == listMainMenu.index('Lihat Semua Directory')):
            allDirectory()
    elif (pilihan-1 == listMainMenu.index('Tambah Directory')):
            newDirectory()
    elif (pilihan-1 == listMainMenu.index('Filter Directory')):
            mainFilterDirectory()
    elif (pilihan-1 == listMainMenu.index('Hapus Directory')):
            deleteDirectory()
    elif (pilihan-1 == listMainMenu.index('Keluar')):
            print('Terimakasih sampai jumpa kembali!!')
            return

# Show the main menu
if True:
    mainMenu()
