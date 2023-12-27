import os
import datetime as dt
import random
import string
os.system('cls')

mahasiswa_tamplate = {
    "nama": "aaaaa",
    "NIM": "111111",
    "prodi": "ttttt",
    "semester": "00",
    "lahir": dt.date(1111,11,11)
}

data_mahasiswa = {}

while True:
    mahasiswa = dict.fromkeys(mahasiswa_tamplate.keys())
    mahasiswa['nama'] = input("nama: ")
    mahasiswa['NIM'] = input('NIM: ')
    mahasiswa['prodi'] = input('Prodi: ')
    mahasiswa['semester'] = input('semester: '.capitalize())
    TAHUN = int(input("tahun lahir: ".capitalize()))
    BULAN = int(input("bulan: ".capitalize()))
    TANGGAL = int(input("tanggal lahir: ".capitalize()))
    mahasiswa['lahir'] = dt.date(TAHUN,BULAN,TANGGAL).strftime('%x')
    
    KEY = "".join((random.choice(string.ascii_uppercase) for i in range(len(mahasiswa))))
    data_mahasiswa.update({KEY:mahasiswa})
    print(data_mahasiswa)

    print(f"\n{'key':<10} {'nama':<15} {'NIM':<16} {'prodi':<10} {'semester':<10} {'Lahir':<15}\n")
    print("="*30) 
    
    
    for data in data_mahasiswa:
        KEY = data
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['NIM']        
        PRODI = data_mahasiswa[KEY]['prodi']        
        SEMESTER = data_mahasiswa[KEY]['semester']
        LAHIR = data_mahasiswa[KEY]['lahir']
        print(f"\n{KEY:<10} {NAMA:<15} {NIM:<16} {PRODI:<10} {SEMESTER:^10} {LAHIR:<15}\n")
        
    tambahData = input("tambah data? [y/n] => ")
    if tambahData == "y":
        tambahData = True
    elif tambahData == "n":
        tambahData == False
        break
        