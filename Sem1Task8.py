# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n,m,k = int(input('1-я сторона: ')),int(input('2-я сторона: ')),int(input('кол-во долек: '))
if k%n == 0 or k%m == 0:
    print('Yes')
else: print('No')
