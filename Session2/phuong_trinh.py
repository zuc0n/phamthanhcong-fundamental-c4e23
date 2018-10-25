a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
phuongtrinh = b**2 - (4 * a * c)
print(phuongtrinh)
if phuongtrinh < 0:
    print("vo nghiem")
elif phuongtrinh == 0: 
    print("x", "=", -b / (2 * a))
else:
    print("x", "=", ((-b - phuongtrinh**1/2) / (2 * a))