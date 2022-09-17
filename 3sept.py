import pymongo


client = pymongo.MongoClient("mongodb+srv://Bindrakesh:rakeshbind24@cluster0.adiwd2u.mongodb.net/?retryWrites=true&w=majority")
db = client.test


data={
    "name" : "rakeshkumar",
    "mail_id" : "rakeshbind@gmail.com",
    "subject" : ["data science" , "big data"]
}
database = client['myinfo']
collection = database["rakesh"]
collection.insert_one(data)

