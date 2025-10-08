'============================ lib.py'
def sum(a: int, b: int):
    return a + b

def div(a: int, b: int):
    return a * b

def x_plus_2(x: int):
    return x + 2

'============================ databse.py'
a = 15
b = 15

result = sum(a, b)

print(result)

'============================ menu.py'
a = input('Введите a: ')
b = input('Введите b: ')

result = sum(int(a), int(b))

print(result)

c = input('Введите c для проверки на четность: ')
result = chislo(int(c))

print(result)