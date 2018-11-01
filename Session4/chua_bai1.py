teen_code = {
    'eny' : 'Em nguoi yeu',
    'ild' : 'Ich liebe dich',
    'any' : 'Anh nguoi yeu',
    'ivd' : 'Ich vermisse dir'
}
while True:
    code = input('Enter your code: ')
    if code in teen_code:
        print(teen_code[code])
    else: 
        bo_sung = input('K thay, ban co muon bo sung k? (Y/N) ').upper()
        if bo_sung == 'Y' or bo_sung == 'YES':
            dinh_nghia = input('Enter your translation: ')
            teen_code[code] = dinh_nghia
        else:
            print(code)
        
    