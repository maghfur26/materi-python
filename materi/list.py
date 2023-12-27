
# menambkaan data ke nilai kahir dari list dengan .append
# lis = []
# # a = input("data untuk list : ")
# data = lis.append(a)

# membuat list dengan range
data = range(0,10,2) # index 0 - 10,urutan = start,stop,increment
print(list(data))

# list dengan for 
data = [i**2 for i in range(0,10,2)] # nilai index akandi pakngkatkan 2
print(data)

# list dengan if
data = [i for i in range(10) if i !=5] # index 5 akan hilang
print(data)

#list bilangan ganjil
data = [i for i in range(0,10) if i%2 !=0]
print(data)
data = [i for i in range(0,10) if i%2 !=1] # genap
print(data)




