import requests

query = "artificial intelligence"
api_key = "26e9167498f54d45a51e0f6eb6e317aa"

url = "https://newsapi.org/v2/everything"
params = {
    "q": query,
    "from": "2026-05-30",
    "sortBy": "publishedAt",
    "apiKey": api_key
}

r = requests.get(url, params=params)
print(r.url)  # see the properly encoded URL

data = r.json()

if data.get("status") != "ok":
    print("API error:", data.get("message"))
else:
    for article in data["articles"]:
        print(article["title"])

