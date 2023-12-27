# awalan nama kelas harus mengunakan huruf besar
class Segitiga:
    '''konstuktror'''
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        
    '''metode'''
    def get_luas(self):
        return 0.5 * self.alas * self.tinggi
    
# segitiga1 = Segitiga(4,5)

# dengan input
tinggi = int(input("tinggi: "))
alas = int(input("alas: "))
segitiga1 = Segitiga(alas, tinggi)

print("luas segitiga: ", segitiga1.get_luas())





