'''tanpa lamda'''
def tambah(**kwargs):
    angka1 = kwargs["angka1"]
    angka2 = kwargs["angka2"]
    hasil = angka1 + angka2
    return hasil

print("Hasil tambah= ", tambah(angka1=5, angka2=3))

'''dengan lambda'''
'''format penulisan: nama_fungsi = lambda argument: expresion(eksekusinya)'''
tambah = lambda angka1,angka2:angka1+angka2
print(tambah(3,5))

'''kegunaan'''

# sort metode biasa
data_list = ["maghfur","irfi","danish"]
data_list.sort()
print("sorted list: ", data_list)

# sort berdasarkan len atau panjang karakter
data_list = ["maghfur","irfi","danish"]

def panjang(nama):
    return len(nama)

data_list.sort(key= panjang)
print(data_list)

# sort menggunakan metode lambda
data_list = ["maghfur","irfi","danish"]

data_list.sort(key= lambda nama:len(nama))
print("sored len by lambda: ", data_list)

# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

def kurang_dari_7(angka):
    return angka < 7

data_angka_new = list(filter(kurang_dari_7,data_angka))
print(data_angka_new)

# genap
list_angka = data_angka.copy()
genap = list(filter(lambda x: x%2 == 0, list_angka))
print("angka genap: ", genap)

# ganjil
ganjil = list(filter(lambda x: x%2 == 1, list_angka))
print("nilai ganjil: ", ganjil)

# kelipatan 3
data_3 = list(filter(lambda x:(x%3==0),data_angka))
print(data_3)

# anonymous function
# currying <- Haskell Curry 

# metode biasa

def pangkat(angka,n):
    hasil = angka**n
    return hasil

hasilPangkat = pangkat(5,2)
print(hasilPangkat)

# dengan currying
def pangkat(n):
    return lambda angka: angka**n

pangkat2 = pangkat(2)
print(pangkat2(5))

pangkat3 = pangkat(3)
print(pangkat3(5))


