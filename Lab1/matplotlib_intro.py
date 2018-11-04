from matplotlib import pyplot

machine_counts = [18,2,30]

machine_names = ['Pc', 'Laptop', 'Mac']
pyplot.title('pc vs laptop vs Mac')
pyplot.pie(machine_counts, labels=machine_names, autopct='%.1f%%', shadow= True, explode = (0.1, 0.1, 0.1))
pyplot.show()