star = "*"
for i in range(1, 10):
    if i%2 == 0:
        print(*star, end ='')
    else:
        print("x", end ='')