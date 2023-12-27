import os
os.system('cls')

'''template'''
# def nama_fungsi(argument):
#       badan fungsi

'''normal function'''
def penambahan():
    a = 1
    b = 2
    print(a + b)
    
penambahan()


'''menggunkan argument yg berada di tanda ()'''
def peserta(nama):
    print("selamat datang saudra", nama)
    
peserta(input("masukan nama: "))


'''function pertambahan'''
def penambahan(angka_ke1,angka_ke2):
    hasil = angka_ke1 + angka_ke2
    print(f"{angka_ke1} + {angka_ke2}= {hasil}")

penambahan(2,3)
penambahan(100,50)

''' function use an input '''
angka_ke1 = int(input("masukan angka ke-1: "))
angka_ke2 = int(input("masukan angka ke-2: "))
penambahan(angka_ke1,angka_ke2)


''' function menggunakan list '''
def hai(nama):
    list_nama = nama.copy()
    for nama in list_nama:
        print("Halo saudara ", nama)
        
keluarga = ["maghfur","irfi","danish"]

hai(keluarga)