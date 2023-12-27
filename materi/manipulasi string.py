# operator in
nama = ("maghfur hasani")
print("maghfur" in nama)

# indexing
nama = ("maghfur hasani")
print("index ke 1 = " + nama[0]) # + untk menambah variable khususu string
print("index ke 2 sampai 6 = ", nama[2:6]) # , untuk memanggil variable dengan tipe bukan hanya string
print(f"index ganjil = {nama[0:10:2]}") #nilai : 2 adalah increment 2 artinya loncat 2 index
print(nama[5:]) # index sesudah lima yg di ambil


# item terkecil
nama = ("maghfur hasani")
print("nilai terkecil adalah ", min(nama)) #nilai terlecil adalah sepasi 
print("nilai terbesar adalah ", max(nama))

# asciicode
ascii_code = ord("m") #melihat nilai dari suatu karakter / char
print(f"nilai ascii code adalah {ascii_code}")
data = 117
print("nilai ascii code adalh ", chr(data))

# operator dalam bentuk metode
nama = ("maghfur hasani")
print(f"jumlah huruf a pada {nama} adalah ", nama.count("a"))
print("nama {1},{0},{2}".format("maghfur","hasani","irfi")) 

# split dan join
saya = ["maghfur","hasani"]
gabungan = "+".join(saya)
print(gabungan)

print("nama saya ", gabungan.split(",")) # menggilangkan tanda + yg tadi sudah di joinkan


# operator dalam bentuk metode 
print(f"huruf a dalam {nama}",nama.count("a"))

# alokasi karakter rjust(),ljust(),center()
tengah = ("maghfur hasani".center(36,"="))
print(tengah)
print(nama.rjust(20)) #akan rata kanan dengan total chr/character 20
print(tengah.strip("=")) #menghilangkan tan = pada variable tengah