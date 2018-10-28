print('Hi there, welcome to superuser gateway')
user = input("Username: ")

while user != 'c4e':
    print("You'r not superuser")
    user = input('Username: ')
else:
    mk = input('Password: ')
    while mk != 'codethechange':
        print('Invalid Password')
        mk = input('Password: ')
    else:
        print('Welcome, c4e')
