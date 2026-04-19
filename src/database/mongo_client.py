from pymongo import MongoClient

def get_mongo_collection():
    """
    Establishes a connection to the MongoDB service running in Docker.
    Returns the specific collection for HR Pro raw data.
    """
    # Connection string to the local MongoDB container on port 27017
    client = MongoClient('mongodb://localhost:27017/')
    
    # Selecting the database 'hr_pro_db' and the collection 'employees_raw'
    # These will be created automatically if they don't exist
    db = client['hr_pro_db']
    return db['employees_raw']

def save_to_mongodb(data, collection):
    """
    Persists the raw message into the MongoDB collection.
    """
    try:
        # Inserting the dictionary directly as a document
        collection.insert_one(data)
    except Exception as e:
        # Error handling in case the connection or insertion fails
        print(f"Error saving to MongoDB: {e}")