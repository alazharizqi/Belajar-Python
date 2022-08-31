# > < >= <= == != is, is not

angka1 = int(input('Masukkan angka pertama : '))
angka2 = int(input('Masukkan angka kedua : '))

lebihdari = angka1 > angka2
kurangdari = angka1 < angka2
lebihdarisamadengan = angka1 >= angka2
kurangdarisamadengan = angka1 <= angka2
samadengan = angka1 == 5
tidaksamadengan = angka1 != 5
iss = angka1 is angka2
issnot = angka1 is not angka2

print('=================')
print(angka1, 'lebih dari', angka2, '=', lebihdari)
print(angka1, 'kurang dari', angka2, '=', kurangdari)
print(angka1, 'lebih dari sama dengan', angka2, '=', lebihdarisamadengan)
print(angka1, 'kurang dari sama dengan', angka2, '=', kurangdarisamadengan)
print(angka1, 'sama dengan', 5, '=', samadengan)
print(angka1, 'tidak sama dengan', 5, '=', tidaksamadengan)
print(angka1, 'is', angka2, '=', iss)
print(angka1, 'is not', angka2, '=', issnot)