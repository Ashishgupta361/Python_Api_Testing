import json

course = '{"name":"AshishGupta", "languages":["Python","Java"]}'
# Loads method parse json string and it returns dictionary
dict = json.loads(course)
#Accessing python directly
print(dict["languages"][1])

with open("test.json") as f:
    data = json.load(f)
    print(type(data))
    print(data)
    print(data['employee'])
    print(data['employee'][0])
    #print(data['employee'][0]['name'])
    # print name of employee with id as 04
    for person in data['employee']:
        if person['id'] == '04':
            print(f"Name of the person with id  is {person['name']} ")

