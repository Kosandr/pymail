#!/usr/bin/python

import requests, json

#https://documentation.mailgun.com/api-sending.html#sending

#r = requests.get('url', auth=('user', 'pass'))
#r.status_code = 200
#r.headers['content-type'] = 'application/json; charset=utf8'
#r.encoding = 'utf-8'
#r.text = "{'x' : 'blahblahblah'}"
#r.json() = {'x' : 'blahblahblah'}

MAIL_URL = 'https://us14.api.mailchimp.com/3.0/'
with open('creds.mailchimp.auth') as f:
   creds = json.loads(f.read())
   uname = creds['uname']
   api_key = creds['priv_key']

def mailchimp_req(path = '', data = None, method='get'):
   fin_url = '%s%s' % (MAIL_URL, path)
   auth = (uname, api_key)

   if method == 'get':
      r_method = requests.get
   elif method == 'post':
      r_method = requests.post

   if method == 'put':
      r_method = requests.put
      r = r_method(fin_url, auth=auth, data = data, headers={'content-type': 'text/json'})
   else:
      r = r_method(fin_url, auth=auth, data = data)

   r_json = r.json()
   #print(r_json)
   return r_json

def get(path = '', data = None):
   return mailchimp_req(path, data, method='get')

def post(path = '', data = {}):
   return mailchimp_req(path, data, method='post')

#d = [api_key, {}, 0, 100, '', '']
#put request = PUT      /campaigns/{campaign_id}/content    Set campaign content

d = {
   'apikey' : api_key,
   'type' : 'html',
   'content' : {
      'html' : '<h1>hi</h1>',
   }
}

#post('generate-text/', d)

#print(mailchimp_req('campaigns/create'))

#post('campaigns/send', data={'apikey': mailchimp.api_key, 'cid': cid})

'''
#list of lists
from mailchimp import get, post, mailchimp_req
import mailchimp

lists_ret = get('lists')
count = lists_ret['total_items']
lists['lists'] = array of actual lists
lists['lists'][0]['id'] = list_id

#list members
list_id = get('lists')['lists'][0]['id']
get('lists/' +  list_id)
get('lists/' + list_id + '/members') #to add, use post


#list of campaigns
campaigns_ret = get('campaigns')
num_items = campaigns_ret['total_items']
campaigns = campaigns_ret['campaigns'] = actual campaigns list
first_campaign_id = campaigns[0]['id']
get('campaigns/' + first_campaign_id) = dict with keys ('send_time', 'emails_sent', 'type', 'content_type', 'receipients')
'''


with open('creds.mailgun.auth') as f:
   mailgun_conf = json.loads(f.read())
   #serv = mailgun_conf['serv']
   #api_key = mailgun_conf['api_key']
default_from = "Business Cape Administrator <admin@businesscape.com>"
default_err = "Report this error to konstantin@businesscape.com"
default_subject = "send_email() without subject. %s" % default_err
default_content = "Error: send_email() called with empty content. %s" % default_err
default_receiver = ["Konstantin Kowalski <konstantin@bussinescape.com"]

#hardcode if forget and lose creds.mailgun.auth
mailgun_conf['serv'] = "https://api.mailgun.net/v3/sandboxb8e5afad79bb4114ab8d3f3d11c15427.mailgun.org/messages"

def send_email_text(sender = default_from, receiver = default_receiver,
               subject = default_subject, content = default_content):
    return requests.post(
        mailgun_conf['serv'],
        auth=("api", mailgun_conf['api_key']),
        data={"from": sender,
              "to": receiver,
              "subject": subject,
              "text": content})

#https://documentation.mailgun.com/api-sending.html#sending
def send_email_html(sender = default_from, receiver = default_receiver,
               subject = default_subject, content = default_content):
    return requests.post(
        mailgun_conf['serv'],
        auth=("api", mailgun_conf['api_key']),
        data={"from": sender,
              "to": receiver,
              "subject": subject,
              "html": content})

receiver = "Konstantin Kowalski <konstantin@businesscape.com>"
html_content = "<h1>Hello this is HTML email test</h1> <img src='http://96bda424cfcc34d9dd1a-0a7f10f87519dba22d2dbc6233a731e5.r41.cf2.rackcdn.com/lakeanimalhospital/lake-animal-hospital/page-photos/img-puppy-kitten-pk.jpg'>"
#send_email_html(subject="Testing sending HTML messages", content=html_content, receiver=receiver)

#send_email()
#"from": "<postmaster@sandboxb8e5afad79bb4114ab8d3f3d11c15427.mailgun.org>",

