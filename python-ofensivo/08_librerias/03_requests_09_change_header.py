#!/usr/bin/env python3

from requests import Request, Session

url = 'https://httpbin.org/get'
s = Session()

headers = {'Custom-Header':'my_custom_header'}

req = Request('GET', url, headers=headers)

prepped = req.prepare()

prepped.headers['Custom-Header'] = 'my_header_changed'
prepped.headers['Another-Header'] = 'other_header'
response = s.send(prepped)

print(response.text)
