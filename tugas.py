import random
import string

rekap_pesanan_makanan = {
    "menu": "aaa", 
    "harga": 1111
    }

list_pesanan = {}

def pesan_makanan():
    '''percabangan makanan'''
    if menu_Makanan == "1":
        list_order["menu"] = "Steak Ayam"
        list_order["harga"] = 25000
        jumlah_pesan = jumlah_pesanan_makanan
    elif menu_Makanan == "2":
        list_order["menu"] = "Steak Sapi"
        list_order["harga"] = 45000
        jumlah_pesan = jumlah_pesanan_makanan
    elif menu_Makanan == "3":
        list_order["menu"] = "Wonton Goreng"
        list_order["harga"] = 15000
        jumlah_pesan = jumlah_pesanan_makanan
    elif menu_Makanan == "4":
        list_order["menu"] = "Wonton Rebus"
        list_order["harga"] = 15000
        jumlah_pesan = jumlah_pesanan_makanan
    elif menu_Makanan == "5":
        list_order["menu"] = "Nasi Goreng"
        list_order["harga"] = 25000
        jumlah_pesan = jumlah_pesanan_makanan
    else:
        print("Nomor menu yang dimasukkan tidak valid!")
    return jumlah_pesan

while True:
    list_order = dict.fromkeys(rekap_pesanan_makanan.keys())
    menu_Makanan = input("menu: ")
    jumlah_pesanan_makanan = input("jumlah: ")
    
    pesan_makanan()
    
    KEY = "".join((random.choice(string.ascii_uppercase) for i in range(len(list_order))))
    
    list_pesanan.update({KEY:list_order})
    print(list_pesanan)
    tambah = input("ada lagi? ")
    
    
    if tambah == "y":
        True
    else:
        False
