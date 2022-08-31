def kuadrat(angka):
    hasil = angka**2
    return hasil

y = kuadrat(5)
print(y)

print(kuadrat(10))

z = 10 + kuadrat(50)
print(z)

def fungsi_tambah(angka1, angka2):
    return angka1 + angka2

x = fungsi_tambah(10, 5)
print(x)

def operasi(angka1, angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2
    return tambah, kurang, kali, bagi

a, b, c, d = operasi(10, 5)


print(f'hasil tambah = {a}')
print(f'hasil kurang = {b}')
print(f'hasil kali = {c}')
print(f'hasil bagi = {d}')