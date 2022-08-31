# +++1---5+++10---15+++

inputt = int(input('Masukkan angka kurang dari 1, 6 sampai 10, dan lebih dari 15 : '))

kurang1 = inputt < 1

lebih1 = inputt > 5

kurang2 = inputt < 11

lebih2 = inputt > 15

benar1 = lebih1 and kurang2

benar2 = kurang1 or lebih2

benar3 = benar1 or benar2

print('Nilai : ', benar3)