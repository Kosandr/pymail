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


