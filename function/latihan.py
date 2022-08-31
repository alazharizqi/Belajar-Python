import os

def header():
    os.system('cls')
    print(f"{'LATIHAN FUNCTION':^40}")
    print(f"{'='*40:^40}")
    print(f'PILIHAN')
    print(f'1. LUAS PERSEGI PANJANG')
    print(f'2. KELILING PERSEGI PANJANG')

def input_user():
    panjang = float(input('Masukkan panjang : '))
    lebar = float(input('Masukkan lebar : '))
    return panjang, lebar

def hitung_luas(panjang, lebar):
    return panjang * lebar

def hitung_keliling(panjang, lebar):
    return 2 * (panjang + lebar)

def hasil(message, value):
    print(f'{message} = {value}')

while True:
    header()
    
    pilihan = input('Masukkan pilihan (1/2)? ')

    if pilihan == '1':
        panjang, lebar = input_user()
        luas = hitung_luas(panjang, lebar)
        hasil('Hasil luas = ', luas)
    elif pilihan == '2':
        panjang, lebar = input_user()
        keliling = hitung_keliling(panjang, lebar)
        hasil('Hasil keliling = ', keliling)
    else:
        print('Inputan tidak dikenal!')

    lanjut = input('Melanjutkan program (y/n)? ')

    if lanjut != 'y':
        break

print('Program sudah selesai')