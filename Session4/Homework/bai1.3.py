size_cuu = [5, 7, 300, 90, 24, 50, 75]
print('Hello, my name is Cris and these are my sheep sizes',size_cuu, sep = '\n')

print('Now my biggest sheep has size',max(size_cuu), "let's shear it.")

vi_tri = size_cuu.index(max(size_cuu))

size_cuu[vi_tri] = 8

print('After shearing, here is my flock', size_cuu, sep = '\n')