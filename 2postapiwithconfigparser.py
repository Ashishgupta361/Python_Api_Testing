import requests
import configparser
from payload import *
from utilities.configurations import *
# calling getconfig method
config = getconfig()
addBook_response = requests.post(config['API']['endpoint']+'/Library/Addbook.php',json=addBookPayload("fered"),
                                 headers={"Content-Type":"application/json"},)

print(addBook_response.json())
response_json = addBook_response.json()
print(type(response_json))

bookId = response_json['ID']
# Delete book
deletebook_response = requests.post(config['API']['endpoint']+'/Library/DeleteBook.php', json={
"ID" : bookId
}, headers={"Content-Type":"application/json"}, )

assert deletebook_response.status_code == 200

res_json = deletebook_response.json()
print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"