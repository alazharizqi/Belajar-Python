def fungsi(nama = 'kamu'):
    print(f'hallo {nama}')

fungsi('jarjar')
fungsi()

def fungsi1(nama, pesan = 'apa kabar?'):
    print(f'hai {nama}, {pesan}')

fungsi1('jarjar', 'gimana kabarnya?')
fungsi1('azhar')

def hitung_pangkat(angka = 10, pangkat = 2):
    hasil = angka ** pangkat
    return hasil

print(hitung_pangkat(5, 2))
print(hitung_pangkat())

hasil = hitung_pangkat(angka=2, pangkat=2)
print(hasil)

def fungsi2(angka1 = 1, angka2 = 2, angka3 = 3, angka4 = 4, angka5 = 5):
    hasil = angka1 + angka2 + angka3 + angka4 + angka5
    return hasil

print(fungsi2())
print(fungsi2(angka5=10))