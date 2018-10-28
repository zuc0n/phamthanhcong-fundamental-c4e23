clothes = ["T-Shirt", "Sweater"]

def print_all_item():
    i = 0
    print("Our items: ", end='')
    while i < len(clothes):
        print(clothes[i], end='')
        if i != len(clothes)-1:
            print(', ', end='')
        i += 1
    print()

while True:
    nhap_vao = input('Welcome to our shop, what do you want (C, R, U, D)? ')
    if nhap_vao == 'R':
        print_all_item()
    elif nhap_vao == 'C':
        new_item = input('Enter new item: ')
        clothes.append(new_item)
        print_all_item()
    elif nhap_vao == 'U':
        pos = input('Update position? ')
        if int(pos) > len(clothes) or int(pos) <= 0 or not pos.isdigit():
            print('Out of range or invalid number')
        else:
            new_item = input('New item? ')
            clothes[int(pos)-1] = new_item
        print_all_item()
    elif nhap_vao == 'D':
        pos = input('Delete position? ')
        if int(pos) > len(clothes) or int(pos) <= 0 or not pos.isdigit():
            print('Out of range or invalid number')
        else:
            clothes.pop(int(pos)-1)
        print_all_item()
    else:
        print('Invalid option')