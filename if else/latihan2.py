print(10*'=','KALKULATOR SEDERHANA',10*'=')
print('')
angka1 = float(input('Masukkan angka 1 : '))
operator = input('Masukkan operator (+,-,x,/) : ')
angka2 = float(input('Masukkan angka 2 : '))
print('')

if operator == '+':
    hasil = angka1 + angka2
    print(f'Hasil penjumlahan {angka1} + {angka2} = {hasil:,}')
elif operator == '-':
    hasil = angka1 - angka2
    print(f'Hasil pengurangan {angka1} - {angka2} = {hasil:,}')
elif operator == 'x' or operator == '*':
    hasil = angka1 * angka2
    print(f'Hasil perkalian {angka1} x {angka2} = {hasil:,}')
elif operator == '/':
    hasil = angka1 / angka2
    print(f'Hasil pembagian {angka1} / {angka2} = {hasil:,}')
else:
    print('Operator tidak dikenal !!!')