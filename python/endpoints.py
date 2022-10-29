import logging
from flask_pymongo import pymongo
from flask import jsonify, request

con_string ="mongodb+srv://hariharan:hariharan@cluster0.fvkufxe.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_string)

db = client.get_database('firstdb')

user_collection = pymongo.collection.Collection(db,'first')
print("Mongodb connected Sucessfully")

def project_api_routes(endpoints):
    @endpoints.route('/connect',methods=['GET'])
    def connect():
        res = 'Welcome to GREAT Karigalan magic show'
        print("Welcome to GREAT Karigalan magic show ")
        return res

    @endpoints.route('/Ulla_vaingada_aparendis',methods=['POST'])
    def Ulla_vaingada_aparendis():
        resp ={}
        try:
            req_body = request.json
            user_collection.insert_one(req_body)
            print("user data stored successfully in the database")
            status ={
                "statusCode":"200",
                "statusMessage":"User Data Stored Successfully in the Database"

            }    
        except Exception as e:
             print(e)
             status={
                 "statusCode":"400",
                "status Message":str(e)
            }
        resp["status"]=status
        return resp

    @endpoints.route('/read-users',methods=['GET'])
    def read_users():
        resp={}
        try:
            users =user_collection.find({})
            print(users)
            status={
                "statusCode":"200",
                "statusMessage":"User Data Retrived Successfully in the Database"
            }
            output=[{'Name':user['unga_appan_vacha_name'],'Email':user['email']}for user in users]
            resp['data']=output
        except Exception as e:
            print(e)
            status ={
                  "statusCode":"400",
                "status Message":str(e)
            }
        resp["status"]=status
        return resp    
    @endpoints.route('/update-user',methods=['PUT']) 
    def update_user():
        resp ={}
        try :
            req_body =request.json
            user_collection.update_one({"id":req_body['id']},{"$set":req_body['update_user_body']})
            print("User Data Updated Successfully in the Database")   
            status={
                 "statusCode":"200",
                "statusMessage":"User Data Updated Successfully in the Database"
            }    
        except Exception as e:
            print(e)
            status ={
                  "statusCode":"400",
                "status Message":str(e)
                
            }
        resp["status"]=status
        return resp

    @endpoints.route('/delete',methods=['DELETE'])
    def delete():
        resp={}
        try:
            delete_id=request.args.get('delete_id')
            user_collection.delete_one({"id":delete_id})
            status={
                  "statusCode":"200",
                "statusMessage":"User Data Deleted Successfully in the Database"
            }
        except Exception as e:
            print(e)
            status ={
                  "statusCode":"400",
                "status Message":str(e)
            }
        resp["status"]=status
        return resp
    return endpoints

    
        

        