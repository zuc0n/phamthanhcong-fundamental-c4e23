from pymongo import MongoClient

uri = "mongodb://admin:admin1@ds249623.mlab.com:49623/c4e23"

# 1 Connect
client = MongoClient(uri)
# 2 Get default database
db = client.get_default_database()
# 3 Get collection
posts = db["posts"]
movies = db["movies"]
# 4 Creat data
new_post = {
    "titles": "Hom nay em xau qua",
    "content": "Nhung ma xinh hon hom qua",
}
new_movie = {
    "title": "Infinity War",
    "Year Release": 2018,
}

# 5 Insert data
# posts.insert_one(new_post)
# movies.insert_one(new_movie)

# 5 Read data
post_list = posts.find()

# p = post_list[2]
for p in post_list:
    print(p["titles"])
    print(p["content"])
    print('------------------')


# 6 Close connection
client.close()