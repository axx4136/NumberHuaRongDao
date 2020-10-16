import json
import requests
import getproblem as gp
import qipan as Qi
url ="http://47.102.118.1:8089/api/challenge/submit"
data = {
    "uuid": gp.Uuid,
    "teamid": 53,
    "token": "99a01c39-f3ee-4967-8b5e-35cfbcfb9f7a",
    "answer": {
        "operations": Qi.operations,
        "swap": Qi.swaplist
    }
}
r = requests.post(url,json=data)
print(r.text)