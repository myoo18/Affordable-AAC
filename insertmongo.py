from pymongo import MongoClient

# Establish a connection to MongoDB
client = MongoClient('mongodb+srv://jyee25:jyee@vthacks.lza3x1j.mongodb.net/')

# Access the 'gridwords' database
db = client['gridwords']

# List of collections
collections = ['adjective', 'noun', 'verb', 'pronoun']

# Iterate through each collection
for col_name in collections:
    collection = db[col_name]
    
    # Iterate through each document in the collection
    for document in collection.find({}):
        word = document['word']
        print(f"Word: {word}")
        
        # Get the image link input from the user
        image_link = input("Enter the image link for this word: ")
        
        # Update the document with the new image link
        collection.update_one({'_id': document['_id']}, {"$set": {"picture": image_link}})

# Close the client connection
client.close()
