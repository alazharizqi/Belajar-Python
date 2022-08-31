x = [1,2]
y = [3,4]

data = [x,y]
data_copy = data.copy()
print(data)
print(data_copy)

# ambil data join list
ambil = data[0]
print(ambil)
ambil1 = data[0][0]
print(ambil1)

#ADDRESS

print(f'Asli : {hex(id(data))}')
print(f'copy : {hex(id(data_copy))}')