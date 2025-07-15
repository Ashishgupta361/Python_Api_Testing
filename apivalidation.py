import json
import requests

response = requests.get("http://216.10.245.166//Library/GetBook.php",
             params={"AuthorName":"Rahul"},)
#print(response.text)
print(type(response.text))
#
# dict_response = json.loads(response.text)
# print(type(dict_response))
# print(dict_response[0]["isbn"])

# json method directly convert into dictionary or list (no need to explicitly convert into dictionary or list )
json_response = response.json()
print(type(json_response))

print(response.status_code)
assert response.status_code == 200

print("Response header: "+f"{response.headers}")

assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

# Retrieve the book details with the  isbn bc3d
for actualBook in json_response:
    if actualBook['isbn'] == 'bc3d':
        print(actualBook)
        break

expected_Book = {'book_name': 'Learn Appium Automation with Java', 'isbn': 'bc3d', 'aisle': '2202'}

assert actualBook == expected_Book
