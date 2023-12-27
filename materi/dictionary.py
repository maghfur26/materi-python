keluarga = {
    "ayah": "ismail",
    "ibu": "mutinah",
    "adik": "danish",
}
print(keluarga["adik"])

# operasi dictionary

# mengecek panjang dictionari
panjang = len(keluarga)
print(panjang)

# mengecek key exist or no
key = "ayah"
exist = key in keluarga
print(exist)

# mengakses value dengan get/khusus untuk dictionary
kk = keluarga.copy()
print(kk.get("ibu"))
# ketika key tidak tersedia,maka akan muncul none,tidak akan eror
print(kk.get("saya","key tidak tersedia"))

# update data 
keluarga.update({"adik":"irfi" + ",danish"}) #mengedit velue dari key tertentu
print(keluarga)
keluarga.update({"saya":"maghfur"})
print(keluarga)

# delete 
kk = keluarga.copy()
del kk["saya"]
print(kk)
