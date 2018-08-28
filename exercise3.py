# def rotate(cube):
#     arr = cube.copy


def test():
    newArray = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    listArray = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    while True:
        userInput = int(input("Masukkan angka: "))
        if userInput % 4 == 1:
            for j, k in zip(range(len(listArray) - 1, -1, -1), range(len(listArray))):
                for l in range(len(listArray)):
                    newArray[l][j] = listArray[k][l]

        elif userInput % 4 == 2:
            for j, k in zip(range(len(listArray) - 1, -1, -1), range(len(listArray))):
                for l, m in zip(range(len(listArray)), range(len(listArray) - 1, -1, -1)):
                    newArray[j][m] = listArray[k][l]

        elif userInput % 4 == 3:
            for j in range(len(listArray)):
                for k, l in zip(range(len(listArray)), range(len(listArray) - 1, -1, -1)):
                    newArray[l][j] = listArray[j][k]
        elif userInput % 4 == 0:
            newArray = listArray
            
        listArray = newArray.copy()
        newArray = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for x in range(len(listArray)):
            print(listArray[x])

test()