fav = ['death note', 'netflix', 'teaching']
print(*fav, sep='\n')
upd = int(input("Vi tri muon xoa?"))
fav.pop(upd - 1)
for i in range(fav):
    print