from pymongo import MongoClient

class Crud:

    def __init__(self):
        self.connection = None
        self.user = None
        self.password = None
        self.database = None
        self.port = None
        self.host = None
        self.protectSheme = True  # This one is for protect database sheme is key is not match with database sheme it will block inserting
        self.safeDelete = True  # This code protect records and prevent delete all records by mistake

    def checkCollection(self, collection_name):
        # This method checks if the given collection name exists in the database, if not it throws an error. 
        # In this way, we encounter a special and easier to fix error, not a Python error.
        try:
            collections = self.connection.list_collection_names()
        except Exception as e:
            return False
        if collection_name in collections:
            return True
        else:
            return False

    def checkColumnName(self, data, collection):
        # This method checks the column names and compares them with the given keys and returns false if a key that does not exist is found.
        # This method is developed to protect data integrity, but its use is designed to be optional. 
        # As long as protectSheme is True, it performs this check, otherwise it does not perform the check.
        myCollection = self.connection[collection]
        document = myCollection.find_one()
        columns = list(document.keys())
        rv = True
        for key in data:
            if key not in columns:
                rv = False
                break
        return rv

    def connect(self):
        if self.user is None:
            raise OSError("you should define user attribute")
        if self.password is None:
            raise OSError("you should define password attribute")
        if self.database is None:
            raise OSError("you should define database attribute")
        if self.port is None:
            raise OSError("you should define port attribute")
        if self.host is None:
            raise OSError("you should define host attribute")
        try:
            client = MongoClient(f'mongodb://{self.user}:{self.password}@{self.host}:{self.port}/')
            self.connection = client[self.database]
        except Exception as e:
            raise Exception(e)

    def create(self, collection, data):
        # This method inserts a record to collection
        if not isinstance(data, dict) or not data:
            raise OSError("Data Type Must be Dictionary Type")
        if not collection:
            raise OSError("Collection name can not be null or empty")
        if not self.checkCollection(collection):
            raise OSError("Collection is not in database")
        if not self.connection:
            raise Exception("You try to insert before connect to database please run connect method before use insert")
        
        check = self.checkColumnName(data, collection)
        if self.protectSheme and not check:
            raise Exception("One or more key in your list is not match column names if you want to continue with this set protectSheme attribute false before")
        
        try:
            myCollection = self.connection[collection]
        except Exception as e:
            raise Exception("Error raised during connect to collection")
        
        try:
            myCollection.insert_one(data)
        except Exception as e:
            raise Exception(f"Error Raised during insert: {e}")
        
        return True

    def read(self, collection, data, limit=0):
        if limit is None or not isinstance(limit, int):
            raise Exception("Limit cannot be null empty or other type than integer")
        if not isinstance(data, dict):
            raise OSError("Data Type Must be Dictionary Type")
        
        try:
            myCollection = self.connection[collection]
        except Exception as e:
            raise Exception("Exception Occurred During connect to collection")
        
        try:
            myReturn = myCollection.find(data).limit(limit)
        except Exception as e:
            raise Exception("Exception Occurred During query")
        
        return list(myReturn)

    def update(self, collection, data, condition):
        if not collection:
            raise Exception("collection name can not be null")
        if not isinstance(data, dict):
            raise Exception("Data must be Dictionary Type")
        if not isinstance(condition, dict):
            raise Exception("Condition must be Dictionary Type")
        if not self.checkCollection(collection):
            raise Exception("Collection is not in database")
        if not self.connection:
            raise Exception("You try to insert before connect to database please run connect method before use insert")
        
        check = self.checkColumnName(data, collection)
        if self.protectSheme and not check:
            raise Exception("One or more key in your list is not match column names if you want to continue with this set protectSheme attribute false before")
        
        try:
            myCollection = self.connection[collection]
        except Exception:
            raise Exception("Exception occurred During connect to collection")
        
        try:
            myData = {"$set": data}
            myReturn = myCollection.update_many(condition, myData)
            
            if not myReturn.acknowledged:
                return False
            else:
                return True
        except Exception:
            raise Exception("Exception Occurred During update Process")

    def delete(self, collection, condition, deleteMany=True):
    	#if condition is empty query will delete all records so if you want to prevent this situation make 
    	#safeDelete attribute True
        if self.safeDelete:
            if not condition:
                raise Exception("Condition Can not be null")
            if not isinstance(condition, dict):
                raise Exception("Condition must be dictionary")
        
        if not collection:
            raise Exception("Collection name Can not be null")
        if not self.checkCollection(collection):
            raise Exception("Collection is not in database")

        try:
            myCollection = self.connection[collection]
        except Exception:
            raise Exception("Exception occurred During connect to collection")
        
        try:
            if deleteMany:
                myReturn = myCollection.delete_many(condition)
            else:
                myReturn = myCollection.delete_one(condition)
            if not myReturn.acknowledged:
            	return False
            else :
            	return True
        except Exception:
            raise Exception

