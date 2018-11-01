stt = [1,2,3,4]
kq = [35,36,40,44]
print('Answer the following algebra question: ')
print('If x = 8, then what is the value of 4(x +3)?')
for c, value in enumerate(kq):
    print(stt[c], value, sep ='. ' )
ctl = input('Your choice: ')
if int(ctl) != 4:
    print(':(')
else: 
    print('Bingo')