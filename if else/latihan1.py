print(10*'=','RUMUS MENGHITUNG',10*'=')
print('''
1. Keliling Persegi
2. Keliling Persegi Panjang
3. Luas Persegi
4. Luas Persegi panjang
5. Volume Kubus
6. Volume Balok
''')
inputt = input('Pilih angka 1 - 6 : ')

print('')

if inputt == '1':
    print(10*'=','KELILING PERSEGI',10*'=')
    s = int(input('Masukkan sisi : '))
    k = s * 4
    print(f'Keliling persegi : {k:,}')

elif inputt == '2':
    print(10*'=','KELILING PERSEGI PANJANG',10*'=')
    p = int(input('Masukkan panjang : '))
    l = int(input('Masukkan lebar : '))
    k = 2 * (p + l)
    print(f'Keliling persegi panjang : {k:,}')

elif inputt == '3':
    print(10*'=','LUAS PERSEGI',10*'=')
    s = int(input('Masukkan sisi : '))
    luas = s * s
    print(f'Luas persegi : {luas:,}')

elif inputt == '4':
    print(10*'=','LUAS PERSEGI PANJANG',10*'=')
    p = int(input('Masukkan panjang : '))
    l = int(input('Masukkan lebar : '))
    luas = p * l
    print(f'Luas persegi panjang : {luas:,}')

elif inputt == '5':
    print(10*'=','VOLUME KUBUS',10*'=')
    s = int(input('Masukkan sisi : '))
    v = s ** 3
    print(f'Volume kubus : {v:,}')

elif inputt == '6':
    print(10*'=','VOLUME BALOK',10*'=')
    p = int(input('Masukkan panjang : '))
    l = int(input('Masukkan lebar : '))
    t = int(input('Masukkan tinggi : '))
    v = p * l * t
    print(f'Volume balok : {v:,}')

else:
    print(10*'=','ANGKA SALAH',10*'=')