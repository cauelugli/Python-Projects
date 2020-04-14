import requests

get = requests.get('http://127.0.0.1:5000').status_code
post = requests.post('http://127.0.0.1:5000/post').status_code
if get == 200:
    print("GET")
if post == 200:
    print("POST")
