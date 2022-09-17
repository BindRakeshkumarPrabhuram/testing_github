import pymongo
client = pymongo.MongoClient("mongodb+srv://Rakeshbind:rakesh2408@cluster0.y8uegym.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]
database = client['inventory']
collection=database['table']
#collection.insert_many(data)
#a = collection.find({'status' : 'A'})
#a = collection.find({'qty' : {'lt' : 100}})
#a=collection.find({'qty': {"$lte": 100}})
#a= collection.find({'item': 'sketch pad','qty':95})
#a=collection.find()
#a=collection.find({'item':'sketch pad','qty' : {'$gte' :95}})
#a = collection.find({'item' : {'$in' : ['postcard' , 'sketch pad']}})
#a = collection.find({'$or': [{'item':'sketch pad'} , {'qty' : 100}]})
#collection.update_one({'item' : 'canvas'} , {'$set' : {'item' : "rakesh"}})
#collection.insert_many([{'item' : "new" } , { 'item' : 'delete'}])
collection.delete_many({'item' : 'new'})
a=collection.find()
for i in a :
    print(i)
