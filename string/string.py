x = 'al'
y = 'azhar'
print(x, y)

nama = 'AL AZHAR'
a = 'A' in nama
b = 'A' not in nama
print(len(nama))
print(a)
print(b)
print(10*'=')
print('index : ', nama[5])
print('range index :', nama[0:5])

nama = 'ajar'
print(min(nama))
print(max(nama))

x = nama.count('a')
print(x)

motor = 'bEaT'
upper = motor.upper()
lower = motor.lower()
print(motor)
print(upper)
print(lower)

bro = 'ajar'
islower = bro.islower()
isupper = bro.isupper()
print('is lower :', str(islower))
print('is upper :', str(isupper))

angka = 5000000000.3588345
f = f"Rp{angka:,.2f}"
print(f)

x = 250

bin = f'{bin(x)}'
oct = f'{oct(x)}'
hex = f'{hex(x)}'

print(x)
print(bin)
print(oct)
print(hex)