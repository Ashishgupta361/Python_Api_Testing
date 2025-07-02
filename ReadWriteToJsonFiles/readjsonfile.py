import json

course = '{"name":"AshishGupta", "languages":["Python","Java"]}'
# Loads method parse json string and it returns dictionary
dict = json.loads(course)
#Accessing name
print(dict["name"])
print(dict["languages"])
list_language = dict["languages"]
# access va;ue inside the list
print(list_language[0])
print(list_language[1])

#Accessing python directly
print(dict["languages"][0])
