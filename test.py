import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"likes": 78, "name": "Joe", "views": 100000},
    {"likes": 100000, "name": "How to Make REST API", "views": 80000},
    {"likes": 780, "name": "Ken greatness", "views": 2000}
]

for i in range (len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())


input()
response = requests.get(BASE + "video/6")
# prints serializable JSON fromatted string
print(response.json())