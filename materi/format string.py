# format string biasa
nama = ("maghfur hasani")
print(f"nama say {nama}")

# format bilangan ribuan
angka = 20000
print(f"angka {angka:,}")

# format decimal
angka = 1246.0000
print(f"angka : {angka:.2f}") # 2f artinya 2 angka setelah titik

# leading zero
print(f"angka : {angka:06.2f}") #angka 06 artinya angka 0 akan menambah dipaling depan angka dan angka 6 adalah panjangnya

# format biner,octal,hexa
a = 19
print(f"bilangan biner dari {a} = ", bin(a))
print(f"bilangan octal dari {a} = ", oct(a))
print(f"bilangan hexa dari {a} = ", hex(a))