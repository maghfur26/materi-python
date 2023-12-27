# output dari kwargs adalah dictionary

'''contoh'''
def peserta(**kwargs):
    nama = kwargs["nama"]
    usia = kwargs["usia"]
    print(f"nama {nama} dengan usia {usia}tahun")
    
peserta(nama="maghfur hasani",usia="23")

'''contoh menggunakan args dan kwargs'''
def math(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output+=angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output*=angka
    return output

hasil = math(1,3,2,4,option="tambah")
print("hasil tambah ", hasil)

hasil = math(1,3,2,4,option="kali") 
print("hasil kali ", hasil)











