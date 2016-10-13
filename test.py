#!/usr/bin/python

import requests

#r = requests.get('url', auth=('user', 'pass'))
#r.status_code = 200
#r.headers['content-type'] = 'application/json; charset=utf8'
#r.encoding = 'utf-8'
#r.text = "{'x' : 'blahblahblah'}"
#r.json() = {'x' : 'blahblahblah'}


with open('key.priv') as f:
   priv_key = f.read()

r = requests.get('https://us14.api.mailchimp.com/3.0/', user=priv_key)
print(r.text)

