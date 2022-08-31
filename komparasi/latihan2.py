#---1+++5---11+++15---
inputt = int(input('Masukkan angka 1 sampai 5 dan 11 sampai 15 : '))

lebih1 = inputt >= 1

kurang1 = inputt <= 5

benar1 = lebih1 and kurang1

lebih2 = inputt >= 11

kurang2 = inputt <= 15

benar2 = lebih2 and kurang2

benar3 = benar1 or benar2

print('Nilai : ', benar3)