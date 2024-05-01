import requests
response = requests.get("https://jsonplaceholder.typicode.com/comments")
print(response.json())

for data in response.json():
    print (data)

