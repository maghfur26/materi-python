''' Type hints untuk fungsi '''

# bentuk standar fungsi yang udah kita pelajari

'''
studi kasus
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)

fungsi(1)
fungsi("Ucup")
fungsi(True)
'''

# penggunaan type hints

import string

def sepuluh_pangkat(argument:int) -> int:
    '''FUNGSI DENGAN HINTS'''
    output = 10**argument
    return output

HASIL = sepuluh_pangkat(4)
print(HASIL)

def display(argument:string):
    print(argument)

display("Ucup")

'''fungsi dengan hints bertujuan agar user tau type data yg harus di inputkan,ketika kita memakai type hints int terus user melakukan input string
di codingan tiadak akan eror tp ketika di run akan eror krn kita sudah menentukan tipe data yang harus di inputkan'''
