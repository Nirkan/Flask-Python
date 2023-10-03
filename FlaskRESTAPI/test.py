import requests

BASE = "http://127.0.0.1:5000/"

"""data = [{"likes": 102, "name":"NK", "views": 90001},
        {"likes": 104, "name":"PK", "views": 10001},
        {"likes": 106, "name":"JK", "views": 20001}] """
"""
for i in range(len(data)):
    response = requests.put(BASE + 'video/' + str(i), data[i])
    print(response.json())
"""

#response = requests.put(BASE + "video/1", {"likes": 10, "name":"Niraj", "views": 10000})
#print(response.json())
#input()

#respnose = requests.delete(BASE + "video/0")
#print(response)
#input()

response = requests.patch(BASE + "video/2", {"views":2123})
print(response.json())
