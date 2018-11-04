from pymongo import MongoClient 
from matplotlib import pyplot

uri ="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

db = client.get_database()

customers = db["customers"]

customers_list = customers.find()
ref_list = []
for c in customers_list:
    ref_list.append(c['ref'])

advs = ref_list.count('ads')
evnt = ref_list.count('events')
woms = ref_list.count('wom')

ref_counts = [advs, evnt, woms]
ref_names = ['Advertisement', 'Events', 'Word of Mouth']

pyplot.title('adv vs events vs wom')
pyplot.pie(ref_counts, labels=ref_names, autopct='%.1f%%', shadow= True, explode = (0,0,0))
pyplot.show()