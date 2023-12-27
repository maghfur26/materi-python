# list bersarang dalam contoh disini kita memsaukan list peserta1 dan peserta2 mejadi 1 kedalam list_peserta,yg kemudian ketika kita mengakses list_peserta maka otomatis peserta1 dan 2 akan kita akses
peserta1 = ["maghfur",24,"ti"]
peserta2 = ["hasani",23,"tk"]

list_peserta = [peserta1,peserta2]
for peserta in list_peserta :
    print(f"nama : {peserta[0]}")
    print(f"usia : {peserta[1]}")
    print(f"prodi : {peserta[2]}")
print(list_peserta)

# mengambil data dari nesteed list
peserta1 = list_peserta[0][0]       #angka [0] pertama adl menunjukan index ke 0 di list_peserta yaitu peserta1 dan angka [0] kedua yaitu index ke 0 dlm peserta1
print("nama peserta pertama = " + peserta1)
peserta2 = list_peserta[1][0]
print("nama peserta kedua " + peserta2)

# copy deep copy
from copy import deepcopy
copy_listPeserta = deepcopy(list_peserta)

copy_listPeserta[0][0] = "irfi"
print("nama peserta pertama adalah ", copy_listPeserta[0][0])