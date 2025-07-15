import requests
import configparser
from payload import *
from utilities.configurations import *
from utilities.resources import *
# calling getconfig method
config = getconfig()
url = config['API']['endpoint']+ApiResources.addbook
headers={"Content-Type":"application/json"}
addBook_response = requests.post(url, json=addBookPayload("fered"), headers=headers,)

print(addBook_response)
print(addBook_response.json())
response_json = addBook_response.json()
print(type(response_json))

bookId = response_json['ID']
# Delete book
config = getconfig()
deletebook_response = requests.post(config['API']['endpoint']+ApiResources.deletebook, json={
"ID" : bookId
}, headers=headers, )

assert deletebook_response.status_code == 200
res_json = deletebook_response.json()
print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"