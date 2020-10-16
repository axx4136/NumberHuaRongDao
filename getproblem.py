import json
import requests
import re
import base64
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3941.4 Safari/537.36',
#     'Content-Type': 'application/json'
# }
# data_json = json.dumps({
#     "teamid":53,
#     "token":"99a01c39-f3ee-4967-8b5e-35cfbcfb9f7a"
# })
# r = requests.post(url, headers=headers, data=data_json)
# print(r.text)


url ="http://47.102.118.1:8089/api/challenge/start/f4f42e09-c7a0-4ab6-90ae-e27eb3baa720"
data = {
    "teamid": 53,
    "token": "99a01c39-f3ee-4967-8b5e-35cfbcfb9f7a"
}
r = requests.post(url,json=data)
r.raise_for_status()
r.encoding = r.apparent_encoding
dic=json.loads(r.text)
img = base64.b64decode(dic["data"]["img"])
Step=dic["data"]["step"]
Swap=dic["data"]["swap"]
Uuid=dic['uuid']
with open("./photo.jpg", "wb") as fp:
    fp.write(img)  # 900*900
