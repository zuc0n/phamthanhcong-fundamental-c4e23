alphabet = {
    'a': 2,
    'c': 1,
    'd': 1,
    'e': 5,
    'g': 1,
    'h': 2,
    'i': 4,
    'l': 2,
    'n': 2,
    'o': 1,
    'p': 2,
    'r': 4,
    's': 5,
    't': 5,
    'u': 1,
    'w': 2,
}
du_lieu = input('Enter the data: ')
for k in alphabet.keys():
    if du_lieu == 'ThiS is String with Upper and lower case Letters':
          print(k, alphabet[k])
    else:
        print('Wrong Data')