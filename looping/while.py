# x = 1
# while x :
#     x += 1
#     print(x)

nama = input('Masukkan nama :')
loop = int(input('Masukkan berapa kali di ulang : '))
x = 0

while x < loop:
    x += 1
    print(f'{x}. {nama}')