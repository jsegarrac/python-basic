import json

import json
person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

# **json.dump()** method can be used for writing to JSON file.

with open('person1.json', 'w') as f:  # writing JSON object
    json.dump(person, f)
    
    
# json.dumps() that helps in converting a dictionary to a JSON object.

# Serializing json  
json_object = json.dumps(person, indent = 4) 
  
# Writing to sample.json 
with open("sample.json", "w") as outfile: 
    outfile.write(json_object) 
    
print(json_object)

