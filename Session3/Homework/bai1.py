print('Hi there, this is superuser gateway')
name = 'c4e'
matkhau = 'codethechange'
user = input('Username: ')
mk = input('Password: ')
if user != name:
    print("You'r not superuser")
else:
    if mk != matkhau:
        print('Password is incorrect')
    else: 
        print('Welcome, c4e')

