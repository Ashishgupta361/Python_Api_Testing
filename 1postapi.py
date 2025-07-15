import requests

addBook_response = requests.post("http://216.10.245.166/Library/Addbook.php",json={
"name":"Learn Appium Automation with Java",
"isbn":"bcvxd",
"aisle":"2297",
"author":"John foe"
}, headers={"Content-Type":"application/json"},)

print(addBook_response.json())
response_json = addBook_response.json()
print(type(response_json))

bookId = response_json['ID']
# Delete book
deletebook_response = requests.post("http://216.10.245.166/Library/DeleteBook.php", json={
"ID" : bookId
}, headers={"Content-Type":"application/json"}, )

assert deletebook_response.status_code == 200

res_json = deletebook_response.json()
print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"