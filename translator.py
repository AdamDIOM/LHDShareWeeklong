import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

original = input("Enter language from ")
to = input("Enter new language ")
text = input("Text to enter ")

payload = "q=" + text + "&source=" + original + "&target=" + to
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': "<API KEY>",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.json()["data"]['translations'][0]['translatedText'])
