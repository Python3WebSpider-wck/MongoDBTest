import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

# client = MongoClient('mongodb://localhost:27017/')

db = client.test
# db = client['test']

collection = db.students

result = collection.find_one({'name': 'Mike'})
print(type(result))
print(result)

from bson.objectid import ObjectId

result = collection.find_one({'_id': ObjectId('65e199aafcd9e131a2f9728c')})
print(result)

results = collection.find({'age': 20})
print(results)
for result in results:
    print(result)

results = collection.find({'age': {'$gt': 20}})
print(results)
for result in results:
    print(result)

results = collection.find({'name': {'$regex': '^M.*'}})
print(results)
for result in results:
    print(result)

# count = collection.find({}).count()
count = collection.count_documents({})
print(f"count = {count}")

count = collection.count_documents({'age': 20})
print(f"count = {count}")

results = collection.find().sort('name', pymongo.ASCENDING)
print([result['name'] for result in results])

results = collection.find().sort('name', pymongo.DESCENDING)
print([result['name'] for result in results])

results = collection.find().sort('name', pymongo.ASCENDING).skip(2)
print([result['name'] for result in results])

results = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
print([result['name'] for result in results])

# from bson.objectid import ObjectId
# collection.find({'_id': {'$gt': ObjectId('593278c815c2602678bb2b8d')}})
