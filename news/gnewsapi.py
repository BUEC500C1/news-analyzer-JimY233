import requests

url = "https://google-news.p.rapidapi.com/v1/topic_headlines"

querystring = {"lang":"en","country":"US","topic":"world"}

headers = {
    'x-rapidapi-key': "c1f803a9afmsh862d3c270d238bep1227a1jsn1ed61da49abe",
    'x-rapidapi-host': "google-news.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)