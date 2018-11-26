import mlab
from river import River

mlab.connect()

river_list = River.objects(continent = "Africa")
for r in river_list:
    print(r.name)