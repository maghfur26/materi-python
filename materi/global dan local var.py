# local scop variable berarti variable berada didalam fungsi,
# semntara global variable berada di luar fungsi

# variable global
x = 10

def fungsi():
    # variable local
    y = 5
    print("Nilai x di dalam fungsi: ", x)
    print("Nilai y di dalam fungsi: ", y)
    
fungsi()

print("Nilai x di dalam fungsi: ", x)
print("Nilai y di dalam fungsi: ", y) #ini akan eror karena menggunakan local scope
