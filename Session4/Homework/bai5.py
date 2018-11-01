stt = [1,2,3,4]
kq = [35,36,40,44]
print('Answer the following algebra question: ')
print('If x = 8, then what is the value of 4(x +3)?')
for c, value in enumerate(kq):
    print(stt[c], value, sep ='. ' )
ctl = input('Your choice: ')
if int(ctl) == 4:
    print('Bingo')
else: 
    print(':(')
    stt2 = [1,2,3,4]
    kq2 = ['About 55', 'About 65', 'About 75', 'About 75']
    print('Estimate the answer (exact caculation not needed): ')
    print('Jack scored these marks in 5 math tests: 49, 81, 72 and 52. What is the meaning? ')
    for m, value2 in enumerate(kq2):
        print(stt2[m], value2, sep ='. ')
    clt2 = input('Your choice: ')
    if int(clt2) != 2:
        print(':(')
        print('You wrongly answer 2 questions')
    else:
        print('Bingo')
        print('You correctly answer 1 out of 2 questions')