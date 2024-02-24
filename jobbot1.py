import pymongo
import json
client=pymongo.MongoClient("mongodb+srv://Yash1234:019lPIWmnWLQ7siI@cluster0.baqxham.mongodb.net/")
#database name is placements
#collections present :- companyname,skill,openings


#inserting data
def insert_json_data(database_name, collection_name, json_file_path):
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)
    db = client[database_name]
    collection = db[collection_name]
    if isinstance(json_data,list):
        collection.insert_many(json_data)
    elif isinstance(json_data,dict):
        collection.insert_one(json_data)
    else:
        print("Invalid Json file format")

#database name is placements
#collections present :- companyname,skill,openings       
# database_name=input()
# collection_name=input()
# insert_json_data(database_name,collection_name,"C:\\Users\\SAMRUDDHI ANIL AHER\\OneDrive\\Documents\\Programming\\Mongo_db tutorial\\openings.json")
#put file name accordingly from where you are coping the data


# getting all docs from particular collection
def get_data(database_name,collection_name):
    db=client[database_name]
    collection=db[collection_name]
    all_docs=collection.find({})
    for i in all_docs:
        print(i)
# database_name=input()
# collection_name=input()
# get_data(database_name,collection_name)
        


#updating data
def update_data(database_name,collection_name):
    db=client[database_name]
    collection=db[collection_name]
    pre={'location':'India'}   #here modify accordingly from which collection which row you want to update 
    next={'$set':{'name':'AWM'}}   #which attribute you want to change from that row in above collection
    up=collection.update_many(pre,next)
    # print(up.modified_count)  #will tell how many things got updated
# database_name=input()
# collection_name=input()
# update_data(database_name,collection_name)
    

# deleting data
def delete_data(database_name,collection_name):
    db=client[database_name]
    collection=db[collection_name]
    #similar as said in updating data
    record={'name':'XYZ'}
    up=collection.delete_one(record)
    print(up.deleted_count)
# database_name=input()
# collection_name=input()
# delete_data(database_name,collection_name)


