count = 1

#FOR
print(10*'=','FOR',10*'=')
for i in range(5):
    print('*'*count)
    count += 1
print(10*'=')

count = 1
#WHILE
print(10*'=','WHILE',10*'=')
while True:
    print('*'*count)
    count += 1

    if count > 10:
        break