import requests
payload = {}

payload["center"] = "Lima"
payload["zoom"] = "10"
payload["size"] = "600x300"
payload["maptype"] = "roadmap"
payload["markers"] = "color:blue|label:S|-12.0548898,-77.0792565"
payload["key"] = "KEY_API_MAP"

url = "https://maps.googleapis.com/maps/api/staticmap"


img = open('google-maps.png','wb')
img.write(requests.get(url, params=payload).content)
img.close()
