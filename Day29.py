from flask import Flask,Response,request
import json
import os
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime
import pymongo
app=Flask(__name__)
mongo_url='mongodb+srv://rithimahesh08_db_user:JIjXuxK0ILfm9w8W@firstcluster.fpjuapg.mongodb.net/'
client = pymongo.MongoClient(
    mongo_url,
    serverSelectionTimeoutMS=5000
)
client.admin.command('ping')
print("MongoDB connected successfully!")
db=client['Reports']
# get for all
# @app.route('/api/v1.0/students', methods=['GET'])
# def students():
#     print("1. GET API CALLED")
#     student = db.students.find()
#     print("2. MongoDB query executed")
#     student_list = list(student)
#     print("3. Records retrieved:", len(student_list))
#     response = dumps(student_list)
#     print("4. JSON conversion completed")
#     return Response(response, mimetype='application/json')
# @app.route('/api/v1.0/students',methods=['GET'])
# def student():
#     student=db.students.find()
#     print('sucess one')
#     return Response(dumps(list(student)),mimetype='application/json')
# @app.route('/api/v1.0/students/<id>',methods=['GET'])
# def single_student(id):
#    student=db.students.find_one({'_id':ObjectId(id)})
#    print('sucess two')
#    return Response(dumps(student),mimetype='application/json')
@app.route('/api/v1.0/students',methods=['POST'])
def create():
   name=request.form['name']
   city=request.form['city']
   age=int(request.form['age'])
   student={
      'name':name,
      'city':city,
      'age':age
   }
   db.students.insert_one(student)
   return Response(dumps({'message':'successful'}),mimetype='application/json',status=201)
@app.route('/api/v1.0/students/<id>',methods=['PUT'])
def up(id):
   query={'_id':ObjectId(id)}
   updated_time=datetime.now()
   student={
      'updated_time':updated_time
   }
   db.students.update_one(query,{'$set':student})
   return Response(dumps({"Message":"Successfully updated"}),mimetype='application/json',status=201)
@app.route('/api/v1.0/students/<id>',methods=['DELETE'])
def delete(id):
        db.students.delete_one({'_id':ObjectId(id)})
        return Response(
            dumps({'message': 'Student deleted successfully'}),
            mimetype='application/json'
        )
if __name__=='__main__':
  port=int(os.environ.get('PORT',5000))
  app.run(debug=True,host='0.0.0.0',port=port)
