# not, or, and, xor

# not
print('===NOT===')
x = True
y = not x
print('nilai x : ',x)
print('nilai y : ',y)

print('===OR===')
# or (jika salah satu ada true, maka hasilnya akan true)
x = True
y = True
z = x or y
print('nilai x : ',x)
print('nilai y : ',y)
print('nilai z : ',z)

print('=========================')

x = False
y = False
z = x or y
print('nilai x : ',x)
print('nilai y : ',y)
print('nilai z : ',z)

print('=========================')

x = True
y = False
z = x or y
print('nilai x : ',x)
print('nilai y : ',y)
print('nilai z : ',z)

print('=========================')

x = False
y = True
z = x or y
print('nilai x : ',x)
print('nilai y : ',y)
print('nilai z : ',z)

print('=========================')

x = False
y = True
z = x or x
print('nilai x : ',x)
print('nilai y : ',y)
print('nilai z : ',z)

print('=========================')

x = False
y = True
z = y or y
print('nilai x : ',x)
print('nilai y : ',y)
print('nilai z : ',z)

print('===AND===')
# and (jika salah satu false, maka hasilnya akan false (kebalikkan dari or))
x = True
y = True
z = x and y
print('nilai x : ',x)
print('nilai y : ',y)
print('nilai z : ',z)

print('=========================')

x = False
y = False
z = x and y
print('nilai x : ',x)
print('nilai y : ',y)
print('nilai z : ',z)

print('=========================')

x = True
y = False
z = x and y
print('nilai x : ',x)
print('nilai y : ',y)
print('nilai z : ',z)

print('=========================')

x = False
y = True
z = x and y
print('nilai x : ',x)
print('nilai y : ',y)
print('nilai z : ',z)

print('=========================')

x = False
y = True
z = x and x
print('nilai x : ',x)
print('nilai y : ',y)
print('nilai z : ',z)

print('=========================')

x = False
y = True
z = y and y
print('nilai x : ',x)
print('nilai y : ',y)
print('nilai z : ',z)

print('===XOR===')
# xor (jika booleannya sama, maka hasilnya akan false, selain itu true)
x = True
y = True
z = x ^ y
print('nilai x : ',x)
print('nilai y : ',y)
print('nilai z : ',z)

print('=========================')

x = False
y = False
z = x ^ y
print('nilai x : ',x)
print('nilai y : ',y)
print('nilai z : ',z)

print('=========================')

x = True
y = False
z = x ^ y
print('nilai x : ',x)
print('nilai y : ',y)
print('nilai z : ',z)

print('=========================')

x = False
y = True
z = x ^ y
print('nilai x : ',x)
print('nilai y : ',y)
print('nilai z : ',z)