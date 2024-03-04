import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)

# client = MongoClient('mongodb://localhost:27017/')

db = client.test
# db = client['test']

collection = db.students
# collection = db['students']

student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

result = collection.insert_many([student1, student2])
print(result)
