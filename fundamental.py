import math

"""
    Basic
"""
# print('Halo')

nama = "andi"
# print(nama)

usia = 23
usia = 32

# print(usia)

jomblo = True

# Data Type

# print(jomblo)
# print(type(nama))
# print(type(usia))
# print(type(jomblo))

"""
    Input
"""

# name = input('Nama kamu?: ')
# age =  input('Umur kamu?: ')
# sex = input('Kelamin kamu?: ')
# occupation = input('Pekerjaan kamu?: ')

# print('Nama: ' + name)
# print('Umur: ' + age)
# print('Kelamin: ' + sex)
# print('Pekerjaan: ' + occupation)


"""
    Arithmetic and Numbers
"""
usiaAndi = 40
usiaBudi = 20

# print(usiaAndi * usiaBudi)
# print(usiaAndi / usiaBudi)
# print(usiaAndi + usiaBudi)
# print(usiaAndi - usiaBudi)
# print(usiaAndi % usiaBudi)
# print(usiaBudi ** 2)

# usiaAndi += 3
# usiaBudi *= 4
# print(usiaAndi)
# print(usiaBudi)

"""
    Math
"""

# print(math.pi) # pi
# print(math.fabs(-4.7)) # absolute math
# print(math.pow(7, 2)) # Kuadrat, dsb
# print(math.sqrt(64)) # Akar

"""
    Strings
"""
# x = 'Halo Dunia Hello'
# print(len(x))
# print(x.index('D'))
# print(x.split())
# print(x.lower())
# print(x.upper())
# print(x.capitalize())
# print(x)

# x1 = "Luthfir"
# x2 = 21

# greet = f"Hi saya {x1}, dan umur saya {x2}"
# print(greet)

"""
    Comparison Object & Logical Operator
"""

x = 5
y = '5'
# print(x == y)
# print(x > int(y))
# print(x < int(y))
# print(x >= int(y))
# print(x <= int(y))
# bool1 = x == y
# bool2 = x >= int(y)
# print(f"boolean 1 = {bool1} dan boolean 2 = {bool2}")
# print(bool1 and bool2)
# print(bool1 or bool2)
# print(not bool1 and bool2)

# if(False):
#     print('Hello')
# else:
#     print('Halo')

"""
    For and While Loops
"""
# number = 1
# while(number <= 10):
#     print(number)
#     number+=1

# for i in range(1, 6):
#     print(i)

# for i in range(10, 50, 10):
#     print(i)


"""
    Notes:
    1. '//' bisa menjadi pengganti math.floor saat melakukan pembagian
"""
"""
    Quiz
"""
# Solve it 1-1

# x = int(input("Masukkan nilai x: "))
# y = int(input("Masukkan nilai y: "))
# z = int(input("Masukkan nilai z: "))

# w = (x + y * z / x * y)
# result = math.pow(int(w), z)
# result = int(result)
# print(result)

# Solve it 2-1
# numberInput = int(input("Masukkan Angka: "))
# result = math.pow(numberInput, 2)
# result = int(result)
# print("Kuadrat dari " + str(numberInput) + " adalah " + str(result))


# Solve it 3-1

# def solveIt3(days):
#     year = math.floor(days / 360)
#     days1 = days % 360
#     month = math.floor(days1/30)
#     days2 = days1 % 30
#     week = math.floor(days2/ 7)
#     day = math.floor(days2 % 7)
     
#     print("years = ",year,
#           "\nmonths = ",month,
#           "\nweeks = ",week,
#           "\ndays = ",day)

# solveIt3(485)


# Solve it 4-1
# ratioAndi = 4/14
# ratioBudi = 10/14

# umurAndi = 49 * ratioAndi + 2
# umurBudi = 49 * ratioBudi + 2

# print(f"umur andi adalah {int(umurAndi)} dan umur budi adalah {int(umurBudi)}")


# Solve it 5-1
# sentences = "i'm a software developer on B corp"
# sentences = sentences.lower()
# countSentences = sentences.count('e')
# print(countSentences)

# Solve it 6-1
# jamAwal = 9
# jarak = 120
# kecepatanTotal = 100/3600
# detikTotal = jarak/ kecepatanTotal
# lamaJam = math.floor(detikTotal // 3600)
# lamaMenit = math.floor((detikTotal % 3600) / 60)
# lamaDetik = math.floor((detikTotal % 3600) % 60)
# print(f"lama Jam {lamaJam} dan lama menit {lamaMenit} dan lama detik {lamaDetik}")
# print(f"Mobil A dan B tertabrak pada pukul {jamAwal + lamaJam}, menit {lamaMenit}, dan detik {lamaDetik}")


# solve it! 1-2
# nilai = int(input("Masukkan angka: "))
# if(nilai % 2 == 0):
#     print(f"Angka {nilai} adalah angka genap")
# else:
#     print(f"Angka {nilai} adalah angka ganjil")

# Solve it! 2-2
# massa = int(input("masukan masa anda(kg): "))
# tinggi = int(input("masukan tinggi anda(cm): "))
# imt = massa/math.pow((tinggi/100), 2)
# if(imt < 18.5):
#     print(f"berat badan anda kurang - {imt}")
# elif(imt >= 18.5 and imt <= 24.9):
#     print(f"berat badan ideal - {imt}")
# elif(imt >= 25.0 and imt <= 29.9):
#     print(f"BB berlebih - {imt}")
# elif(imt >= 30.0 and imt <= 39.9):
#     print(f"BB sangat berlebih - {imt}")
# else:
#     print(f"Obesitas - {imt}")

"""
    For and While Loops
"""
# number = 1
# while(number <= 5):
#     print(number)
#     number+=1

# listItem = list(range(1, 11, 2))
# print(listItem)

# for x in listItem:
#     print(x)


# Solve it For Loops
# for i in range(1, 11):
#     print(f"Nomor urut {i}")

# Solve it For loops with 3 param
# for i in range(0, 21, 2):
#     print(f"Nomor Urut {i}")

# for i in range(1, 20, 2):
#     print(f"Nomor urut {i}")

# Solve it For loop drawing
# i = ''

# for item in range(5):
#     for item1 in range(5):
#         i += " * "
#     i += "\n"

# print(i)

# Solve it draw
# i = ""
# for item in range(0, 5):
#     for item1 in range(0, item+1):
#         i += " * "
#     i += "\n"

# print(i)

"""
    Function and List
"""

# def contoh():
#     print('Halo Dunia')

# contoh()
# x = 10
# y = 50

# def contoh():
#     print(x+y)

# contoh()

# def myName(name):
#     print(f"{name} susilo")

# myName('Luthfir')

# def data(x, y):
#     print(f"{x} lahir tahun {y}")

# data('Adi', 1990)

# def total(x, y):
#     z = x + y
#     return z

# print(total(4, 9))
# def kali (x):
#     if(x < 2):
#         return 1
#     else:
#         return x * tiga()

# print(kali(5))

# def tiga():
#     return 3

# Recursive Function

# def pangkat(x, y):
#     if(y == 1):
#         return x
#     else:
#         y -= 1
#         return x * pangkat(x, y)

# print(pangkat(2, 4))

# def kali(x = 5, y = 2):
#     return x * y

# print(kali(y=4))

listMobil = ['Alya', 'Xenia', 'Avanza']

# print(listMobil)
# print(listMobil[0])

# listMobil[1:] = ['Xpander', 'Livina']
# print(listMobil)
# for x in listMobil:
#     print(x)
# print(listMobil[0:3])

# buah = ['Nanas', 'Apel', 'Jeruk', 'Pir', 'Melon']
# buah[0] = 'Buah Naga'
# buah.pop()
# print(buah)

# listTest = [1, 'hi', ['hello', 2, True, [0, 1]]]
# print(listTest[2][3][1:])

"""
    Lambda Exp, Tuples, etc
"""

# Dictionaries
# d = {
#     "key1": "item1",
#     "key2": "item2",
#     "kucing": [
#         3,
#         "jerapah"
#     ]
# }

# print(d["key1"])
# print(d["kucing"][0])

# Dictionaries inside Dictionaries
# d = {
#     "key1": {
#         "key2": "item2"
#     },
#     "kucing": [
#         3,
#         "jerapah"
#     ]
# }
# print(d["key1"])
# print(d["key1"]["key2"])

# Tuples
# t = (
#     1, # Data Pertama
#     [
#         0,  
#         "test"
#     ], # Data Kedua
#     {
#         "a1": True,
#         "a2": [
#             1,
#             "mark",
#             "dark"
#         ]
#     }, # Data Ketiga
#     (
#         True,
#         {
#             "person1": "luthfir"
#         }
#     )
# )

# print(t)

# a = "test1"
# b = 20

# d = { "" + a + "": 5, "" + str(b) + "": 9, "maruk": [7, 8]}

# for item in d:
#     print(item)
# for item in d:
#     print(d[item])

# d["keren"] = 70
# print(d)
# Sets (didalam sets tidak bisa ada list atau dict, tetapi bisa ada tuples, karena bersifat hashable/ tidak bisa diubah)

# s = {1, 2, 3, 4, 3, 1, 3, 2}

# print(s)
# print(list(s))

# newList = [1, 3, 3, 2, 1, 2, "test1", "test1", "test2"]
# s = set(newList)

# print(s)

#List comprehension
# listNum = [1, 2, 3, 4, 5]
# listNum = [item * 2 for item in listNum]

# print(listNum)

# Lambda Expressions
# def times2(num):
#     return num * 2

# print(times2(2))

# lambda num: num * 2

# map
# without lambda

# def times2(num):
#     return num * 2

# listNum = [1, 2, 3, 4, 5]
# listNum = list(map(times2, listNum))
# print(listNum)

# with lambda

# listNum = [1, 2, 3, 4, 5]
# listNum = list(map(lambda num: num * 2, listNum))
# print(listNum)

# Filter

# without lambda
# def genap(num):
#     return num % 2 == 0

# listNum = [1, 2, 3, 4, 5]
# listNum = list(filter(genap, listNum))
# print(listNum)

# with lambda

# listNum = [1, 2, 3, 4, 5]
# listNum = list(filter(lambda num: num % 2 == 0, listNum))
# print(listNum)

# numList = [1,2,3]
# input = 'x'
# check1 = input in numList
# check2 = 'x' in ['x','y','z']
# check3 = 'KA' in 'kurakas'
# print(check1)
# print(check2)
# print(check3)

"""
    Algorithm
"""

# def fizzBuzz(integer):
#     for x in range(1, integer+1):
#         if x % 3 == 0 and x % 5 == 0:
#             print("fizzbuzz")
#         elif x % 3 == 0:
#             print("fizz")
#         elif x % 5 == 0:
#             print("buzz")
#         else:
#             print(x)

# fizzBuzz(30)

# def fibo(urut):
#     listData = [1, 1]
#     for i in range(2, urut):
#         listData.append(listData[i-2] + listData[i-1])
#     return listData[urut-1], listData
# print(fibo(100))

# import math
# def reverseList(theList) :
#     for i in range(math.floor(len(theList)/2)) :
#         tempList = theList[i]
#         theList[i] = theList[len(theList) - 1 - i]
#         theList[len(theList) - 1 - i] = tempList
#     return theList
# print(reverseList([6,4,5,2,3]))

# mean

theList = [1, 2, 3, 2, 5, 2, 7, 3, 3, 4, 4, 4]
#  
# import statistics
# mode = statistics.mode(theList)
# print(mode)

# def mean(theList):
#     hasil = 0
#     for x in theList:
#         hasil += x
#     print(hasil/len(theList))
# mean(theList)

# median
# def median(thelist):
#     thelist.sort()
#     median = 0
#     if len(thelist) % 2 != 0:
#         median = thelist[math.floor(len(thelist)/2)]
#     else:
#         mid1 = thelist[(int(len(thelist) / 2)) - 1]
#         mid2 = thelist[int(len(thelist) / 2)]
#         median = (mid1 + mid2) / 2
#     return median

# print(median(theList))

# Mode
# def mode(thelist):
#     mostCommon = max(map(thelist.count, thelist))
#     listSet = set(filter(lambda x: thelist.count(x) == mostCommon, thelist))
#     check = list(listSet)
#     if len(check) > 1:
#         return "This Array have no mode"
#     else:
#         return check[0]

# print(mode(theList))


# Solve it 1-3
# number = int(input("Masukkan angka: "))
# i = ""
# for item in range(number, 0, -1):
#     for item1 in range(0, item):
#         i += " * "
#     i += "\n"

# print(i)

# Solve it 2-3
# number = int(input("Masukkan angka: "))
# i = ""
# for item in range(number, 0, -1):
#     for item1 in range(0, item):
#         i += " * "
#     i += "\n"

# for item in range(1, number):
#     for item1 in range(0, item+1):
#         i += " * "
#     i += "\n"

# print(i)

# Solve it 3-3
# number = int(input("masukkan angka: "))
# z=""
# for num in range(number):
#     for num1 in range(0, number-1-num):
#         z+=" "
#     for num in range(0, (num*2)+1):
#         z+= "*"
#     z+="\n"
# print(z)

# solve it 4-3
# space = 0

# for i in range(19, 0, -2):
#     print(' '*space + i*'*')
#     space +=1

# Solve it 5-3
# space = 9
# for i in range(1, 10, 2):
#     print(' '*space + i*'*')
#     space-=1
# for i in range(11, 0, -2):
#     print(' '*space + i*'*')
#     space+=1

# Solve it 1-4

# maself
# arrayList = [200, 10, 20, 3, 1, 8]
# newArray = []

# def sort(theList, sortType):
#     if sortType.lower() == 'asc' and theList != []:
#         while arrayList:
#             minimumNumber = arrayList[0]
#             for x in arrayList:
#                 if x < minimumNumber:
#                     minimumNumber = x
#             newArray.append(minimumNumber)
#             arrayList.remove(minimumNumber)
#     elif sortType == 'desc' and theList != []:
#         while arrayList:
#             minimumNumber = arrayList[0]
#             for x in arrayList:
#                 if x > minimumNumber:
#                     minimumNumber = x
#             newArray.append(minimumNumber)
#             arrayList.remove(minimumNumber)
#     else:
#         print('Value yg anda masukkan salah atau kurang!')

# sort(arrayList, 'awdaw')
# print(newArray)


# Bubble Sort
# def sort(listSort, sortType):
#     if sortType.lower() == 'asc'  and listSort != []:
#         for i in range(len(listSort)):
#             for x in range(i+1, len(listSort)):
#                 if listSort[i] > listSort[x]:
#                     temp = listSort[i]
#                     listSort[i] = listSort[x]
#                     listSort[x] =  temp
#     elif sortType.lower() == 'desc' and listSort != []:
#         for i in range(len(listSort)):
#             for x in range(i+1, len(listSort)):
#                 if listSort[i] < listSort[x]:
#                     temp = listSort[i]
#                     listSort[i] = listSort[x]
#                     listSort[x] =  temp
#     else:
#         print('Value yg anda masukkan salah atau kurang!')

# array = [900, 20, 1000, 1, 8, 8, 7, 20]

# sort(array, 'desc')

# print(array)

# Solve it 2-4
# anotherArray = [400, 1000, 900, 250, 125, 110]
# anotherList = []

# def searchMaxandMinValue(theList):
#     maxValue = theList[0]
#     minValue = theList[0]
#     for x in theList:
#         if x < minValue:
#             minValue = x
#         elif x > maxValue:
#             maxValue = x
#     anotherList[:] = [minValue, maxValue]

# searchMaxandMinValue(anotherArray)
# print(anotherList)

# solve it 1 - 5
# searchList = ['Merdeka', 'Hello', 'Hellos', 'sohib', 'Kari Ayam']
# print(searchList)
# searchValue = []
# searchInput = input("Search: ")
# def search():
#     for x in searchList:
#         check = searchInput.lower() in x.lower()
#         if check:
#             searchValue.append(x)
#         else:
#             print('Tidak ada data')
#             break
#     print(searchValue)
# search()

# Mr. Baron
# listData = ['Merdeka', 'Hello', 'Hellos', 'sohib', 'Kari Ayam']
# print(listData)
# inputUser = input('Search: ')
# def searchList(keyword, theList):
#     newList = list(filter(lambda item: keyword.lower() in item.lower(), theList))
#     return newList

# searchedList = searchList(inputUser, listData)
# print(searchedList)
