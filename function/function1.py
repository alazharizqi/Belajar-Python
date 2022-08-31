def fungsi(nama):
    print(f'halo {nama}')

fungsi('jarjar')
fungsi('zharsuke')

def tambah(angka1, angka2):
    hasil = angka1 + angka2
    print(f'{angka1} + {angka2} = {hasil}')

tambah(100, 900)
tambah(485, 7834)

def absen(list_pelajar):
    data_pelajar = list_pelajar.copy()
    for pelajar in data_pelajar:
        print(f'nama pelajar {pelajar}')

member = ['jarjar', 'zharsuke', 'azhar']

absen(member)