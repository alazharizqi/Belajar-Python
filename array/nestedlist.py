data1 = [1,2,3,4,5]
data2 = [6,7,8,9,10]
Sum = sum(data1)
avg = Sum / len(data1)
print(data1)
print(f'Menjumlahkan data list : {Sum}')
print(f'Rata - rata data list : {avg}')
data1.reverse()
print(f'Reverse data 1 : {data1}')
print(data2)

datanested = [data1, data2]
print(datanested)

user1 = ['azhar', 19, 'Laki-laki']
user2 = ['zharsuke', 19, 'Laki-laki']
listuser = [user1, user2]
print(listuser)

for i in listuser:
    print(f'nama : {i[0]}')
    print(f'umur : {i[1]}')
    print(f'jenis kelamin : {i[2]} \n')