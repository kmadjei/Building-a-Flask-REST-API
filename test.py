import requests

BASE = "http://127.0.0.1:5000/"

# data = [
#     {"likes": 78, "name": "Joe", "views": 100000},
#     {"likes": 100000, "name": "How to Make REST API", "views": 80000},
#     {"likes": 780, "name": "Ken greatness", "views": 2000}
# ]


response = requests.patch(BASE + "video/2", {"view": 99})
# prints serializable JSON fromatted string
print(response.json())

