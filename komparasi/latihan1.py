# CASE BUAT NILAI TRUE KURANG DARI 5 DAN LEBIH DARI 10
print(10*'=', 'CASE OR', 10*'=')
inputt = int(input('Masukkan angka kurang dari 5 atau lebih dari 10 : '))

kurang = inputt < 5

lebih = inputt > 10

benar = kurang or lebih

print('Nilai : ', benar)

# KESIMPULANNYA JIKA FALSE DIMULAI DARI ANGKA 5 - 10

# CASE MEMBUAT IRISAN 5 - 10
print(10*'=', 'CASE AND', 10*'=')

inputt = int(input('Masukkan angka antara 5 - 10 : '))

lebih = inputt >= 5

kurang = inputt <=10

benar = lebih and kurang

print('Nilai : ', benar)

# KESIMPULANNYA AKAN TRUE JIKA NILAI 5 - 10