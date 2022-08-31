# PROGRAM LIST BUKU

list_buku = []

print(10*'=','PROGRAM LIST BUKU', 10*'=', '\n')
while True:
    judul = input('Masukkan judul buku : ')
    penulis = input('Masukkan penulis buku : ')

    data_buku = [judul, penulis]
    list_buku.append(data_buku)
    print('')
    for index, i in enumerate(list_buku):
        print(f'No. {index+1} | {i[0]} | {i[1]}')

    ex = input('\nInput buku lagi ? (y/n) : ')

    if ex != 'y':
        break