import requests

url = "https://matchilling-tronald-dump-v1.p.rapidapi.com/random/quote"

headers = {
	"Accept": "application/hal+json",
	"X-RapidAPI-Key": "cac018b0f0mshfb0de045d8543dap144acejsn39e1183e038e",
	"X-RapidAPI-Host": "matchilling-tronald-dump-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.json()["value"])


for data in response.json()["data"]:
     print(data["value"])