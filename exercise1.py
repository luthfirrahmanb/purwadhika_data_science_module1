listMainMenu = ['1. Lihat Menu', '2. Lihat Cart', '3. Checkout', '4. Keluar']
listHokbenMenu = ['1. Paket Hoki A Rp.20000', '2. Paket Hoki B Rp.25000', '3. Paket Hoki C Rp.30000']
listTombolCart = ['0. Kembali ke Main Menu', '1. Hapus semua Pesanan']
listTombolCheckout = ['0. Kembali ke Main Menu']
listPesanan = []

"""
    Sub Menu
"""
# Menu Item
def menuItem():
    print("\nMenunya:\n")
    for x in listHokbenMenu:
        print(x)
    
    pilihan = int(input("Masukkan Pilihan: "))
    if(pilihan-1 == listHokbenMenu.index('1. Paket Hoki A Rp.20000')):
        listPesanan.append('Paket Hoki A Rp.20000')
        mainMenu()
    if(pilihan-1 == listHokbenMenu.index('2. Paket Hoki B Rp.25000')):
        listPesanan.append('Paket Hoki B Rp.25000')
        mainMenu()
    if(pilihan-1 == listHokbenMenu.index('3. Paket Hoki C Rp.30000')):
        listPesanan.append('Paket Hoki C Rp.30000')
        mainMenu()

# Menu Cart
def menuCart():
    if(listPesanan == []):
        print("cart kosong\n\n")
        print(listTombolCart[0])
        pilihan = int(input("Masukkan Pilihan: "))
        if (pilihan == listTombolCart.index('0. Kembali ke Main Menu')):
            mainMenu()
    else:
        print("\nCart:\n")
        for i, x in enumerate(listPesanan):
            print(f"{i+1}. {x}")
        print("\n\n")
        print("Pilihan")
        for y in listTombolCart:
            print(f"{y}")
        pilihan = int(input("Masukkan Pilihan: "))
        if (pilihan == listTombolCart.index('0. Kembali ke Main Menu')):
            mainMenu()
        if (pilihan == listTombolCart.index('1. Hapus semua Pesanan')):
            deleteAllData()

# Menu Checkout
def menuCheckout():
    if(listPesanan == []):
        print("Checkout kosong\n\n")
        print(listTombolCheckout[0])
        pilihan = int(input("Masukkan Pilihan: "))
        if (pilihan == listTombolCheckout.index('0. Kembali ke Main Menu')):
            mainMenu()
    else:
        listHarga = []
        print("\nCheckout:\n")
        for i, x in enumerate(listPesanan):
            print(f"{i+1}. {x}")
            listHarga.append(int(x[16:]))
        Total = sum(listHarga[0:len(listHarga)])
        print(f"Total Harga: {Total}")
        totalMoney = int(input("Masukkan Jumlah Uang: "))
        if(totalMoney < Total):
            print("uang tidak cukup")
            menuCheckout()
        elif(totalMoney >= Total):
            change = totalMoney - Total
            print(f"kembalian anda {change}")
            deleteAllData()

"""
    Delete All Data
"""
def deleteAllData():
    listPesanan.clear()
    mainMenu()


"""
    Main Menu
"""
def mainMenu():
    print("\nHalo Selamat datang di Hoki-Hoki Bento \n\nMain Menu:")
    for x in listMainMenu:
        print(x)
    pilihan = int(input("Masukkan Pilihan: "))
    if (pilihan-1 == listMainMenu.index('1. Lihat Menu')):
            menuItem()
    elif (pilihan-1 == listMainMenu.index('2. Lihat Cart')):
            menuCart()
    elif (pilihan-1 == listMainMenu.index('3. Checkout')):
            menuCheckout()
    elif (pilihan-1 == listMainMenu.index('4. Keluar')):
            print('Terimakasih sampai jumpa kembali!!')
            return

"""
    Main Page
"""
if(True):
    mainMenu()