list = [1,2,3,4,5]

for i in list:
    print(f'i ke {i}')
print(10*'=', '\n')

for i in range(5):
    print(f'i ke {1+i}')
print(10*'=')

string = 'ajar'
for i in string:
    print(i)
print(10*'=')

user = ['zharsuke', 'azhar', 'sasuke', 'naruto', 'sakura', 'kakashi']
for i in user:
    if i == 'sasuke':
        break
    print(i)
print(10*'=')
for i in user:
    if i == 'sasuke':
        continue
    print(i)