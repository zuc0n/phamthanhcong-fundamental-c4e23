fav = ['death note', 'netflix', 'teaching']
print(*fav, sep='\n')
upd = int(input("Vi tri muon thay doi?"))
new_fav = input("So thich moi?")
fav[upd - 1] = new_fav
print(*fav, sep ='\n')