'''fungsi return akan mengambil nilai atau value dari variable tertentu sehingga nantinya bisa dilakukan manipulasi'''

def penambahan(nilai1,nilai2):
    '''penambahan'''
    hasil = nilai1 + nilai2
    return hasil

nilaiAkhir= penambahan(3,6)
print("Hasil 3 + 6 = ", nilaiAkhir)

''' fungsi dengan return banyak '''
def aritmatika(angka1,angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2
    return tambah,kurang,kali,bagi

var1,var2,var3,var4 = aritmatika(4,5)

print("hasil 4 + 5= ", var1)
print("hasil 4 - 5= ", var2)
print("hasil 4 x 5= ", var3)
print("hasil 4 : 5= ", var4)

