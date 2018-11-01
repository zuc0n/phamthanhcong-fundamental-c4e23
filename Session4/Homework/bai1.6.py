size_cuu = [5, 7, 300, 90, 24, 50, 75]
print('Hello, my name is Cris and these are my sheep sizes',size_cuu, sep = '\n')
for i in range(1,5):
    print('Thang', i)
    
    for i in range(len(size_cuu)):
        size_cuu[i] += 50
        
    print('One month has passed, now here is my flock',size_cuu, sep = '\n')
    print('Now my biggest sheep has size',max(size_cuu), "let's shear it.")
    vi_tri = size_cuu.index(max(size_cuu))
    size_cuu[vi_tri] = 8
    print('After shearing, here is my flock', size_cuu, sep = '\n')
tong = sum(size_cuu)
cash = tong * 2
print('My size has size in total: ',tong)
print('I would get',tong,'* 2$','=',cash,'$')