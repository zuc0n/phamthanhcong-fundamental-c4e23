from pymongo import MongoClient

uri ="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

db = client.get_default_database()

posts = db['posts']

new_post = {
    'title': 'A Song of Fire anh Ice',
    'Author': 'George R.R. Martin',
    'Content': 'Ich habe Nichts ueber C4E23 zu sagen', 
}

posts.insert_one(new_post)

client.close()