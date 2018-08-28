# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:54:27 2018

@author: Amri's Dell
"""
def inputList(rep):
    """
    filters input using .isdigit() method to accept numericals only.
    .isalnum() to accept alpha and numerical values
    .isalpha() for alphabets
    .isnumeric() the same with .isdigit() ?
    .isspace() for only spaces
    """
    while True:
        angka = input("Masukkan angka: ")
        if angka.isdigit():
##            insert angka into the rep list. Either use for loops and append, or add list with list
#            for i in [str(each) for each in list(angka)]:
#                rep.append(i)
            rep += list(angka)
            return rep
        else:
            print("\nMasukkan ulang!")

def lihatList(angka):
    """
    angka must be a list of numbers in string
    """
    upper = {"0":' _ ', "1":"   ", "2":" _ ", "3":" _ ", "4":"   ", "5":" _ ", "6":" _ ", "7":" _ ", "8":" _ ", "9":" _ "}
    middle ={"0":'| |', "1":"  |", "2":" _|", "3":" _|", "4":"|_|", "5":"|_ ", "6":"|_ ", "7":"  |", "8":"|_|", "9":"|_|"}
    lower = {"0":'|_|', "1":"  |", "2":"|_ ", "3":" _|", "4":"  |", "5":" _|", "6":"|_|", "7":"  |", "8":"|_|", "9":" _|"}
    atas, tengah, bawah = "", "", ""
    for i in angka:
        atas += upper[i]
        tengah += middle[i]
        bawah += lower[i]
    print(f"{atas}\n{tengah}\n{bawah}")

def resetList(rep):
#    rep = []
    rep.clear()
    print("\nIsi list telah dihapus.")
    return rep

def mainMenu(rep = []):
    rep = rep.copy()
    while True:
        inputUser = input("Selamat datang di app Seven Segment. \nMain menu: \n1.Isi list angka (0-9) \n2.Lihat list \n3.Reset list \n4.Keluar \n\nSilahkan pilih opsi: ")
        if inputUser == "1":
            rep = inputList(rep)
        elif inputUser == "2":
            lihatList(rep)
        elif inputUser == "3":
            resetList(rep)
        elif inputUser == "4":
            print("\n... Asalkan kau bahagiaaaa")
            return rep
 
mainMenu()
