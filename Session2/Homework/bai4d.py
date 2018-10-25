n = int(input("nhap so = "))
star = "*"
for i in range(1, n+1):
    if i%2 == 0:
        print(*star, end ='')
    else:
        print('x', end ='')