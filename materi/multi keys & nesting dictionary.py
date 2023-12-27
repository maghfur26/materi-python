import datetime as dt

mahasiswa1 = {
    "nama": "maghfur hasani",
    "NIM": "17230490",
    "prodi": "Teknologi informasi",
    "lahir": dt.datetime(1999,11,26)
}

mahasiswa2 = {
    "nama": "irfi yanda abidin",
    "NIM": "17230490",
    "prodi": "Teknologi informasi",
    "lahir": dt.datetime(2003,4,8)
}

dataMahasiswa = {
    "data1" : mahasiswa1,
    "data2" : mahasiswa2
}

print("-"*58)
print(f"{'key':<9} {'nama':<19} {'prodi':<20} {'lahir':<9}")
print("-"*58)

for mahasiswa in dataMahasiswa:
    KEY = mahasiswa
    NAMA = dataMahasiswa[KEY]['nama']
    PRODI = dataMahasiswa[KEY]['prodi']
    LAHIR = dataMahasiswa[KEY]['lahir'].strftime('%x')
    print(f"{KEY:<9} {NAMA:<19} {PRODI:<20} {LAHIR:<9}")