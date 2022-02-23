#Example Python Code to Insert a Document
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,user,password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:37736'%(user,password))
        self.database = self.client['AAC']

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data) 
            print("animal entered")
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
    #Create method to implement the R in CRUD 
    def read(self, data):
        if data is not None:
            data = self.database.animals.find(data,{"_id":False})    
            return data
        else:
            raise Exception("nothing to read, data parameter is empty")

     # Update method for U in CRUD
    def update(self, original_data, update_data):
        if original_data is not None and update_data is not None:
            return self.database.animals.update(original_data, {"$set": update_data})
        else:
            raise Exception("Update failed, please input correctly both document data and update data")
        
            
    #Delete method for D in CRUD
    def delete(self, data):
        if data is not None:
            _data = self.read(data) #makes sure animal exists to delete
            if _data is None:
                print("Animal not found")
                return
            #if found delete the animal or animals
            self.database.animals.delete_many(_data) 
            print("animal deleted")
            return
        else:
            raise Exception("nothing to read, hint is empty")
            
   