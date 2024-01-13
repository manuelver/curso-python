#!/usr/bin/env python3

import requests

url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are="working")

response = requests.get(url, cookies=cookies)

print(response.text)

