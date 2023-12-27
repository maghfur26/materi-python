# *args digunakan ketika ada banyak arguments yang mau digunakan,untuk mempeprmudah kita gunakan
# *args

# TANP *args
def kalimat(nama,usia,alamat):
    print(f"nama {nama} usia {usia} asal {alamat}")
    
kalimat("maghfur",23,"Bantrbolang")

# membuat list tanpa *args
def data_list(list):
    data= list.copy()
    nama = data[0]
    usia = data[1]
    alamat = data[2]
    print(f"nama {nama} usia {usia} asal {alamat}")

data_list(["maghfur hasani",24,"Bantarbolang"])

# dengan *args
def list_data(*args):
    nama = args[0]
    usia = args[1]
    alamat = args[2]
    print(f"nama {nama} usia {usia} asal {alamat}")

list_data("maghfur", 23, "Bantarbolang") # normal
list_data(input("masukan nama:"), int(input("usia: ")), input("Almat: ")) # dengan input

