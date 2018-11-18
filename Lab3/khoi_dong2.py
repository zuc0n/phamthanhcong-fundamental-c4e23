a = int(input('Nhap so a = '))
b = int(input('Nhap so b = '))
op = input('Operation(+,-,*,/): ')
while True:
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a*b)
    elif op == '/':
        print(a / b)
    break