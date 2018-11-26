import mlab
from river import River

mlab.connect()


river_list = River.objects(continent= "S. America", length__lt= 1000)
for r in river_list:
    print(r.name)

