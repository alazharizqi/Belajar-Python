# MANIPULASI LIST

# INDEX   0      1       2(-1)
data = ['al', 'azhar', 'rizqi']
print(data)
data0 = data[0]
print(data0)
lastdata = data[-1]
print(lastdata)
panjangdata = len(data)
print(panjangdata)

nama = ['azhar', 'zharsuke', 'asep']
for i in nama:
    print(i)
    
## MACAM" METHOD PADA LIST
print(nama)
nama = ['azhar', 'zharsuke', 'asep']
nama.append('jarjar') #menambah data di posisi terakhir
print(nama)

nama = ['azhar', 'zharsuke', 'asep']
nama.clear() #MENGHAPUS SEMUA DATA
print(nama)

nama = ['azhar', 'zharsuke', 'asep']
x = nama.copy() #mengcopy data list
print(f'copy : {x}')

nama = ['azhar', 'zharsuke', 'asep']
x = nama.count('zharsuke') # untuk menghitung ada berapa banyak datanya
print(x)

nama = ['azhar', 'zharsuke', 'asep']
motor = ['beat', 'vario', 'mio']
nama.extend(motor) #menggabungkan data dengan 2 variable yang beda
print(nama)

nama = ['azhar', 'zharsuke', 'asep']
x = nama.index('azhar') # untuk mengetahui posisi index data
print(x)

nama = ['azhar', 'zharsuke', 'asep']
nama.insert(0, 'jajar') # untuk menambah data sesuai dengan posisi index
print(nama)

nama = ['azhar', 'zharsuke', 'asep']
nama.pop(2) # untuk menghapus data sesuai dengan posisi index
print(nama)

nama = ['azhar', 'zharsuke', 'asep']
nama.remove('azhar') # menghapus data dengan value
print(nama)

nama = ['azhar', 'zharsuke', 'asep']
nama.reverse() # untuk membalik posisi data 
print(nama)

nama = ['azhar', 'zharsuke', 'asep']
nama.sort() # untuk mengurutkan data
print(nama)

nama = ['azhar', 'zharsuke', 'asep']
nama [0] = 'kakashi' # mengubah data dengan posisi index
print(nama)