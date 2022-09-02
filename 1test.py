import pymongo

client = pymongo.MongoClient("mongodb+srv://ineuron:Rakesh%402408@cluster0.fbkxmjz.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d={
    "name":"rakesh",
    "email":"rakesh@gmail.com",
    "surname" : "bind"
}
db1 = client['1test']
coll = db1['test']
coll.insert_one(d)