#!/usr/bin/python

import requests, json

creds_path = '/sec/creds/'
creds_fname = '/creds.mailgun.auth'

with open(creds_path + creds_fname) as f:
   mailgun_conf = json.loads(f.read().replace('\n', ''))
   #serv = mailgun_conf['serv']
   #api_key = mailgun_conf['api_key']

default_from = "Business Cape Administrator <admin@businesscape.com>"
default_err = "Report this error to konstantin@businesscape.com"
default_subject = "send_email() without subject. %s" % default_err
default_content = "Error: send_email() called with empty content. %s" % default_err
default_receiver = ["Konstantin Kowalski <konstantin@businesscape.com>"]

#hardcode if forget and lose creds.mailgun.auth
mailgun_conf['serv'] = "https://api.mailgun.net/v3/businesscape.com/messages"

def convert_recv(recv):
   if typeof(recv) is str:
      return recv
   elif typeof(recv) is list:
      return recv[:]

def send_email_text(sender = default_from, receiver = default_receiver,
                    subject = default_subject, content = default_content):

   receivers = convert_recv(receiver)

   return requests.post(
      mailgun_conf['serv'],
      auth=("api", mailgun_conf['api_key']),
      data={"from": sender,
            "to": receivers,
            "subject": subject,
            "text": content})

#https://documentation.mailgun.com/api-sending.html#sending
def send_email_html(sender = default_from, receiver = default_receiver,
                    subject = default_subject, content = default_content):

   receivers = convert_recv(receiver)

   return requests.post(
      mailgun_conf['serv'],
      auth=("api", mailgun_conf['api_key']),
      data={"from": sender,
            "to": receivers,
            "subject": subject,
            "html": content})

receiver = "Konstantin Kowalski <konstantin@businesscape.com>"
html_content = "<h1>Hello this is HTML email test</h1> <img src='http://96bda424cfcc34d9dd1a-0a7f10f87519dba22d2dbc6233a731e5.r41.cf2.rackcdn.com/lakeanimalhospital/lake-animal-hospital/page-photos/img-puppy-kitten-pk.jpg'>"
#send_email_html(subject="Testing sending HTML messages", content=html_content, receiver=receiver)

#send_email()
#"from": "<postmaster@sandboxb8e5afad79bb4114ab8d3f3d11c15427.mailgun.org>",

