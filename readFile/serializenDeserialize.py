"""
Serialization is serialize (convert) a Python object (data) (Basic types (dict, list, str, int)	in json) and Almost all Python objects
in pickle)  into a binary format and save it persistently in a file named data.pkl.

In short, this approach is essential for scenarios where you want to save, share, or reuse Python objects efficiently and conveniently.

Following it with reading (deserialization) lets your program restore the saved objects back into memory exactly as they were.
uses data paersistance, reduce recomputation, data excahnge, state saving, effiecnty

"""


import pickle ## Step 1: Import pickle module to perform serialization
import json

#data to serialize
data = { 'name': 'Alice', 'age': 30, 'city': 'New York' }

#serialize data to a file
"""When open('data.pkl', 'wb') is called, Python opens the file named data.pkl in binary write mode.If the file data.pkl does not exist in the current directory, Python automatically creates an empty file with that name"""

with open('data.pkl', "wb") as file: # Step 5: Open (or create) a file named 'data.pkl' in binary write mode ('wb')
    pickle.dump(data, file) # serializes the data object and writes it to this file
    #or json.dump(data, file) # you can use json also

print("data.pkl file created")

#load serialized data from file
with open('data.pkl', 'rb') as file: # # Step 6: Open the 'data.pkl' file in binary read mode ('rb') to load the serialized data
    loaded_data = pickle.load(file) # Step 7: Deserialize data from file back into Python object
    #or loaded_data = json.load(file) # you can use json also
    print(loaded_data) #  Print the deserialized data, which will be the original dictionary