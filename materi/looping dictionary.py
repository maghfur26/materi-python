keluarga = {
    "ayah":"ismail",
    "ibu":"mutnah",
    "adik":["irfi","danish"]
}

# looping standar
for data in keluarga:
    print(data) #yg keluar adalah keys
print()

# mengambil item(keys and value)
gabungan = " ".join(keluarga["adik"]) # ini untuk menggabungkan spasi dengan keluarga["adik"]
keluarga["adik"] = gabungan # agar ketika di print object/keys berubah seperti yang telah di joinkan
for data in keluarga.keys():
    print(keluarga.get(data))
print()

# mengambil value
for value in keluarga.values():
    print(value)
print()

# mengambil berdasarkan kelompok dengan items
for item in keluarga.items():
    print(" : ".join(item))
# print()
# mengambil item dan value secara terpisah
keluarga = keluarga.copy()
for key,value in keluarga.items():
    print(f"key = {key}, value = {value}")