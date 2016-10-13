#!/usr/bin/python

import requests, json

#r = requests.get('url', auth=('user', 'pass'))
#r.status_code = 200
#r.headers['content-type'] = 'application/json; charset=utf8'
#r.encoding = 'utf-8'
#r.text = "{'x' : 'blahblahblah'}"
#r.json() = {'x' : 'blahblahblah'}

with open('creds.auth') as f:
   creds = json.loads(f.read())
   uname = creds['uname']
   priv_key = creds['priv_key']

r = requests.get('https://us14.api.mailchimp.com/3.0/', auth=(uname, priv_key))
print(r.text)

