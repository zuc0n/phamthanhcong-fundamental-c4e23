n = int(input("n = "))
m = int(input("m = "))
star ="*"
for i in range(n):
    for i in range(m):
        print(*star, end="")
    print()
    