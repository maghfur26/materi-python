# segitiga siku kiri
angka = int(input("masukan nilai : "))
for i in range(0,angka+1) :
    for j in range(0,i+1) :
        print(j, end=" ")
    print(" ")

print(" ")

# segitiga siku kanan
angka = 8
for i in range(0,angka):
    for j in range(0, i):
        print("  ",end="")
    for j in range(0,angka):
        print("*",end=" ")
    angka-=1
    print(" ")

print(" ")
# segitiga sama kaki atas 
angka = 8
for i in range(0,angka):
    for j in range(0, i):
        print(" ",end="")
    for j in range(0,angka):
        print("*",end=" ")
    angka-=1
    print(" ")

print(" ")
# segitiga sama kaki bawah
angka = 8
for i in range(0,angka+1) :
    for j in range(angka - i):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()
