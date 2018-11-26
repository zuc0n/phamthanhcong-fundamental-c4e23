import mlab
from movies import Movie
from resource import Resource

from faker import Faker



# for _ in range(500):
#     print(faker.city())

mlab.connect()

# m = Movie.objects().with_id('5bf8018dfb6fc0561fff7dbd')

# print(m)
# m.delete()

# movie_list = Movie.objects()


# # for m in movie_list:
# #     print(m.year, m.image, m.title, sep="\n")

# resource_list = Resource.objects()

# for r in resource_list:
#     print(r.name, r.yob, r.city, r.weight, r.height, sep="\n")


# m.save()

# r = Resource(name="Pham Thanh Cong", city="Hanoi", yob=1996, height=175, weight=65)

# r.save()

# m = Movie.objects().with_id('5bf805fffb6fc0561fff8078')
# if m is None:
#     print('Not found')
# else:
#     print('found')
#     m.delete()

# m = Movie.objects().first()
# m.delete()
from random import randint
faker = Faker()
# for _ in range(100):
#     name = faker.name()
#     city = faker.state()
#     yob = randint(1953,2000)
#     height = randint(150, 210)
#     weight = randint(60, 150)
#     r = Resource(name= name, city= city, yob= yob, height= height, weight= weight)
#     r.save()


# records = Resource.objects(name= 'Jacob Carter')
# for r in records:
#     print(r.city)
#     print(r.weight)
#     print(r.height)

# records = Resource.objects(height= 172)
# print(len(records))
# for r in records:
#     print(r.name)
#     print('------------------')

# records = Resource.objects(height__lt=200, name__icontains="Sarah")
# print(len(records))

# records = Resource.objects()

# for r in records:
#     r.update(set__available=False)
# r = Resource.objects().with_id("5bf80d6df9f9532648752ec5")
# r.update(set__available=True)