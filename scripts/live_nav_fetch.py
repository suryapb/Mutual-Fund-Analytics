import requests
url="https://api.mfapi.in/mf/125497"
response=requests.get(url)
print(response.status_code)
data=response.json()
print(data.keys())
print(data["status"])
print(data["meta"])
print(type(data["data"]))
print(data["data"][0])