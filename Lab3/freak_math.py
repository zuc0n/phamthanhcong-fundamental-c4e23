from random import randint

x = randint(0,10)
y = randint(0,10)
z = randint((x+y)-3, (x+y)+3)
tg  = x+y
print(a,'+',b,'=',z)
anw = input('T/F? ')
print(anw)
if anw == 'T' and (tg-z) == 0:
    print('Yay')
if anw == 'T' and (tg-z) != 0:
    print('Wrong')
if anw == 'F' and (tg-z) == 0:
    print('Wrong')
if anw == 'F' and (tg-z) != 0:
    print('Yay')