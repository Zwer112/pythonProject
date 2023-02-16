

f1, f2 = 1, 1

while f1 < 100000:
    print(f1, sep=' ', end=' ')
    print(f2, sep=' ', end=' ')
    nf1 = f1 + f2
    f1 = nf1
    f2 = f1 + f2
print('Finish')



def summa(a, b):
    """Описание функции """
    if isinstance(a, int) and isinstance(b, int):
        return a + b * a ** b
    return 'error'

print (summa('aas', 1))
print(summa(a=2, b=85))

