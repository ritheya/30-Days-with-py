import pymongo
from flask import Flask,render_template
import os 
mongo_URl='mongodb+srv://rithimahesh08_db_user:JIjXuxK0ILfm9w8W@firstcluster.fpjuapg.mongodb.net/'
client=pymongo.MongoClient(mongo_URl)
print(client.list_database_names())
db=client['Reports']
db.students.insert_one({'name':'Rithi','age':20,'city':'theni'})
students=[{
    'name':'Rithi','age':20,'city':'theni'},{'name':'abi','age':20,'city':'madurai'},{'name':'Anei','age':20,'city':'mangdi'},{'name':'Rani','age':20,'city':'tanjore'}]
for student in students:
 db.students.insert_many([{'name':'Rithi','age':20,'city':'theni'},{'name':'abi','age':20,'city':'madurai'},{'name':'Anei','age':20,'city':'mangdi'},{'name':'Rani','age':20,'city':'tanjore'}])
app=Flask(__name__)
if __name__=='__main__':
    port=int(os.environ.get('PORT',5000))
    app.run(debug=True,host='0.0.0.0',port=port)



import pymongo
from flask import Flask,render_template
import os 
from bson.objectid import ObjectId
mongo_URl='mongodb+srv://rithimahesh08_db_user:JIjXuxK0ILfm9w8W@firstcluster.fpjuapg.mongodb.net/'
client=pymongo.MongoClient(mongo_URl)
db=client['Reports']
# student=db.students.find_one() or by id in db
stud=db.students.find({},{'_id':0,'name':1})
for student in stud:
 print(student)
app=Flask(__name__)
if __name__=='__main__':
    port=int(os.environ.get('PORT',5000))
    app.run(debug=True,host='0.0.0.0',port=port)




import pymongo
from flask import Flask,render_template
import os 
from bson.objectid import ObjectId
mongo_URl='mongodb+srv://rithimahesh08_db_user:JIjXuxK0ILfm9w8W@firstcluster.fpjuapg.mongodb.net/'
client=pymongo.MongoClient(mongo_URl)
db=client['Reports']
query={'age':20}
stud=db.students.find().sort('name')
stud=db.students.find().sort('name',1)
stud=db.students.find().limit(2)
quer={'city':'theni'}
new_value={'$set':{'country':'India'}}
db.students.update_one(quer,new_value)
query={'name':'Rithi'}
db.students.delete_many(query)
for student in db.students.find():
 print(student)
app=Flask(__name__)
if __name__=='__main__':
    port=int(os.environ.get('PORT',5000))
    app.run(debug=True,host='0.0.0.0',port=port)
# to drp db.students.drop()