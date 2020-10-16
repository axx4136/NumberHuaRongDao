import json
import requests
url ="http://47.102.118.1:8089//api/challenge/create"
data = {
    "teamid": 53,
    "data": {
        "letter": "y",
        "exclude": 6,
        "challenge": [
            [0, 5, 9],
            [4, 8, 1],
            [2, 3, 7]
        ],
        "step": 5,
        "swap": [3,8]
    },
    "token": "99a01c39-f3ee-4967-8b5e-35cfbcfb9f7a"
}
r = requests.post(url,json=data)
print(r.text)