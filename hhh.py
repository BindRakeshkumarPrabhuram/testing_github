import pymongo

#client = pymongo.MongoClient("mongodb+srv://ineuron:Rakesh%402408@cluster0.fbkxmjz.mongodb.net/?retryWrites=true&w=majority")
#db = client.test
client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


