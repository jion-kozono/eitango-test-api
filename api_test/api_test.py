import json
import requests

from constants.url import URL

def testPostIsCorrect():
    data = [
        {
            "id": "ID:1",
            "is_correct": 1,
        },
        {
            "id": "ID:2",
            "is_correct": -1,
        },
    ]
    res = requests.post(
        f'{URL}/isCorrect/',
        data=json.dumps(data)
    )
    print(res.status_code)

if __name__ == '__main__':
    testPostIsCorrect()