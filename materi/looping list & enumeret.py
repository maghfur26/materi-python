# for 
data = [3,4,5,6,0,7]
for i in data :
    print(f"angka = {i}")

# for in range
data = [3,4,5,6,0,7]
panjang = len(data)
print("\nfor in range")
for i in range(panjang) :
    print("angka ke ", data[i])

# while
couunter = 0
print("\nwhile")
while couunter < panjang :
    print(f"angka ", data[couunter])
    print("good") 
    couunter +=1
    #disini ketika index yg dimasuka adalah [i] maka hasilnya adl 7 krn i sudah di isi oleh perulangan for terakhir yg mengisinya yaitu dia sampai ke index ke 5 dan index ke 5 berisi 7

# list comprehention 
keluarga = ["maghfur","irfi","danish","ismail","mutinah"]
[print (f"nama {nama}") for nama in keluarga]

# enumeret
keluarga1 = keluarga.copy()
for index,data in enumerate(keluarga1) :
    print(f"index = {index}     data = {data}")
# untuk mengecek index dan data dari suatu list