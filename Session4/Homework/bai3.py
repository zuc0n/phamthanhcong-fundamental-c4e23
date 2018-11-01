price = {}
price['banana'] = 4
price['apple'] = 2
price['orange'] = 1.5
price['pear'] = 3

stock = {}

stock['banana'] = 6
stock['apple'] = 0
stock['orange'] = 32
stock['pear'] = 15

for k in price.keys():
    print(k)
    print('price: ', price[k])
    print('stock: ', stock[k])

total = 0

for k in price.keys():
    print(price[k] * stock[k])
    total += int(price[k] * stock[k])
print(total)