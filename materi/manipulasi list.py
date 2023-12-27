# menambahkan data sesuai index
keluarga = ["maghur","ismail","mutinah","irf"]
keluarga.insert(2,"danish") # index ke 2 akan digantikan,angka 2 merupakan posisi index yg akan digantikan 
print(keluarga)

# menambahkan list ke list menggunakan .extend()
data_baru = ["danish"]
keluarga.extend(data_baru) 
print(keluarga)

# merubah index tertentu
keluarga[0] = "tahu"
print(keluarga)

# menghapus data berdasarkan nama datanya
keluarga.remove("tahu")
print(" ".join(keluarga))

# menambahkan index ke urutn akhir
keluarga.append("irfi")
print(keluarga)

# remove data berdasarkan index
nama = ["maghfur","hasani","danish"]
print(nama.pop())
print(nama)
