# Project
print('''
------------ Program Kasir Semeja Waroenk ------------
           ================================
          |   Daftar Menu Semeja Waroenk   |
          |================================|
          |  No | Menu Makanan | Harga     |    
          |-----|--------------|-----------|
          |  1  | Steak Sapi   | Rp. 45.000|
          |  2  | wonton Goreng| Rp. 15.000|
          |  3  | Wonton Nyemek| Rp. 15.000|
          |  4  | Dimsum Ayam  | Rp. 15.000|
          |  5  | Pangsit Kuah | Rp. 20.000|
          |  6  | Mie Jebew    | Rp. 15.000|
          |  7  | Basreng      | Rp. 5.000 |
          |================================|
          |  No | Menu Minuman | Harga     |
          |-----|--------------|-----------|
          |  8  | Es Teh Leci  | Rp. 15.000|
          |  9  | Jus Jeruk    | Rp. 15.000|
          |  10 | Cappucino    | Rp. 25.000|
          |  11 | Air Mineral  | Rp. 5.000 |
           ================================
''')

pembeli = input("Nama Pembeli : ")
menu_Makanan = input("Masukkan nomor menu makanan (1-7): ")
jumlah_pesan_Makanan = int(input("Masukan jumlah pesan makanan : "))

# Lakukan percabangan berdasarkan pilihan pengguna
if menu_Makanan == "1":
    menu_makanan_nama = "Steak Sapi"
    menu_makanan_harga = 45000 * jumlah_pesan_Makanan
elif menu_Makanan == "2":
    menu_makanan_nama = "Wonton Goreng"
    menu_makanan_harga = 15000 * jumlah_pesan_Makanan
elif menu_Makanan == "3":
    menu_makanan_nama = "Wonton Nyemek"
    menu_makanan_harga = 15000 * jumlah_pesan_Makanan
elif menu_Makanan == "4":
    menu_makanan_nama = "Dimsum Ayam"
    menu_makanan_harga = 15000 * jumlah_pesan_Makanan
elif menu_Makanan == "5":
    menu_makanan_nama = "Pangsit Kuah"
    menu_makanan_harga = 20000 * jumlah_pesan_Makanan
elif menu_Makanan == "6":
    menu_makanan_nama = "Mie Jebew"
    menu_makanan_harga = 15000 * jumlah_pesan_Makanan
elif menu_Makanan == "7":
    menu_makanan_nama = "Basreng"
    menu_makanan_harga = 5000 * jumlah_pesan_Makanan
else:
    print("Nomor menu yang dimasukkan tidak valid!")

menu_Minuman = input("Masukkan nomor menu minuman (8-11): ")
jumlah_pesan_Minuman = int(input("Masukan jumlah pesan minuman : "))

# Lakukan percabangan berdasarkan pilihan pengguna
if menu_Minuman == "8":
    menu_minuman_nama = "Es Teh Leci"
    menu_minuman_harga = 15000 * jumlah_pesan_Minuman
elif menu_Minuman == "9":
    menu_minuman_nama = "Jus Jeruk"
    menu_minuman_harga = 15000 * jumlah_pesan_Minuman
elif menu_Minuman == "10":
    menu_minuman_nama = "Cappucino"
    menu_minuman_harga = 25000 * jumlah_pesan_Minuman
elif menu_Minuman == "11":
    menu_minuman_nama = "Air Mineral"
    menu_minuman_harga = 5000 * jumlah_pesan_Minuman
else:
    print("Nomor menu minuman yang dimasukkan tidak valid!")

print('''
----------------------------------
''')  
tanya = input ("Ingin Menambah Pesanan? (y/t) : ")

print('''
----------------------------------
''') 


if tanya == "y" :
    tambahan_makanan = input("Masukkan nomor menu makanan tambahan (1-7): ")
    jumlah_pesan_makanan_Tamb = int(input("Masukan jumlah pesan makanan : "))
    if tambahan_makanan == "1" :
        menu_makanan_nama_tamb = "Steak Sapi"
        menu_makanan_harga_tamb = 45000 * jumlah_pesan_makanan_Tamb
    elif tambahan_makanan == "2":
        menu_makanan_nama_tamb = "Wonton Goreng"
        menu_makanan_harga_tamb = 15000 * jumlah_pesan_makanan_Tamb
    elif tambahan_makanan == "3":
        menu_makanan_nama_tamb = "Wonton Nyemek"
        menu_makanan_harga_tamb = 15000 * jumlah_pesan_makanan_Tamb
    elif tambahan_makanan == "4":
        menu_makanan_nama_tamb = "Dimsum Ayam"
        menu_makanan_harga_tamb = 15000 * jumlah_pesan_makanan_Tamb
    elif tambahan_makanan == "5":
        menu_makanan_nama_tamb = "Pangsit Kuah"
        menu_makanan_harga_tamb = 20000 * jumlah_pesan_makanan_Tamb
    elif tambahan_makanan == "6":
        menu_makanan_nama_tamb = "Mie Jebew"
        menu_makanan_harga_tamb = 15000 * jumlah_pesan_makanan_Tamb
    elif tambahan_makanan == "7":
        menu_makanan_nama_tamb = "Basreng"
        menu_makanan_harga_tamb = 5000 * jumlah_pesan_makanan_Tamb
    elif tambahan_makanan == "-":
        menu_makanan_nama_tamb = "-"
        menu_makanan_harga_tamb = 0 * jumlah_pesan_makanan_Tamb
    else:
        print("Nomor menu yang dimasukkan tidak valid!")

    tambahan_minuman = input("Masukkan nomor menu minuman tambahan (8-11): ")
    jumlah_pesan_minuman_Tamb = int(input("Masukan jumlah pesan minuman : "))
    if tambahan_minuman == "8":
        menu_minuman_nama_tamb = "Es Teh Leci"
        menu_minuman_harga_tamb = 45000 * jumlah_pesan_minuman_Tamb
    elif tambahan_minuman == "9":
        menu_minuman_nama_tamb = "Jus Jeruk"
        menu_minuman_harga_tamb= 15000 * jumlah_pesan_minuman_Tamb
    elif tambahan_minuman == "10":
        menu_minuman_nama_tamb = "Cappucino"
        menu_minuman_harga_tamb = 15000 * jumlah_pesan_minuman_Tamb
    elif tambahan_minuman == "11":
        menu_minuman_nama_tamb = "Air Mineral"
        menu_minuman_harga_tamb = 15000 * jumlah_pesan_minuman_Tamb
    elif tambahan_minuman == "-":
        menu_minuman_nama_tamb = "-"
        menu_minuman_harga_tamb = 0 * jumlah_pesan_minuman_Tamb
    else:
        print("Nomor menu yang dimasukkan tidak valid!")
elif tanya ==  "t" :
    print("Silakan lanjut untuk pembayaran")
    menu_makanan_nama_tamb = "-"
    menu_makanan_harga_tamb = 0
    menu_minuman_nama_tamb = "-"
    menu_minuman_harga_tamb = 0
    jumlah_pesan_makanan_Tamb = 0
    jumlah_pesan_minuman_Tamb = 0
else:
    print("Input tidak valid. Silakan masukkan 'y' jika ingin menambah pesanan atau 't' jika tidak.")

# Hitung total keseluruhan jumlah pesanan
total_harga_semua = menu_makanan_harga + menu_minuman_harga
+ menu_makanan_harga_tamb + menu_minuman_harga_tamb

# Tampilkan struk pembayaran
print('''
=================== Daftar Menu Yang Dipesan ====================
''')
print("Nama Pembeli            : ", pembeli)
print("Menu Makanan            : ", menu_makanan_nama )
print("Jumlah Makanan          :  "      + str (jumlah_pesan_Makanan))
print("Harga Makanan           :  Rp." + str (menu_makanan_harga))
print("Menu Minuman            : ", menu_minuman_nama)
print("Jumlah Minuman          :  "      + str (jumlah_pesan_Minuman))
print("Harga Minuman           :  Rp." + str (menu_minuman_harga))
print("Menu Makanan Tambahan   : ", menu_makanan_nama_tamb )
print("Jumlah Makanan Tambahan :  "      + str (jumlah_pesan_makanan_Tamb))
print("Harga Makanan Tambahan  :  Rp." + str (menu_makanan_harga_tamb))
print("Menu Minuman Tambahan   : ",  menu_minuman_nama_tamb )
print("Jumlah Minuman Tambahan :  "      + str (jumlah_pesan_minuman_Tamb))
print("Harga Minuman Tambahan  :  Rp." + str (menu_minuman_harga_tamb))
print("Total                   :  Rp." + str (total_harga_semua ))
print()

print("-"*46)
pembayaran = input("Lanjut pembayaran? (y/t): ")
print("-"*46)

if pembayaran == "y":
    uang = int(input("\nmasukan uang: "))
    kembalian = uang - total_harga_semua
    print(f"Kembalian   : {kembalian:,}")
    print()
    print("-"*46)
else:
    print("TERIMAKASIH ATAS KUNJUNGANNYA".center(46))