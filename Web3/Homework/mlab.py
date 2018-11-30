import mongoengine
# mongodb://<dbuser>:<dbpassword>@ds039261.mlab.com:39261/movie
host = "ds039261.mlab.com"
port = 39261
db_name = "movies"
user_name = "CristianPham"
password = "dnhhoa0702"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())