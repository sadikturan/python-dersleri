import requests

headlines_url = "https://newsapi.org/v2/top-headlines"
everything_url = "https://newsapi.org/v2/everything"

api_key = "<api_key>"


# response = requests.get(headlines_url, params={
#     "apiKey": api_key,
#     "country": "tr"
# })

response = requests.get(everything_url, params={
    "apiKey": api_key,
    "q": "futbol",
    "language": "tr",
    "sortBy": "publishedAt"
})

haberler = response.json()["articles"]

for i in haberler:
    print(i["source"]["name"])
    print(i["title"])
    print(i["url"])