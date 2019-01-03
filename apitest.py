# Requirements
# - Have Python installed
# - Install pipenv
# - Install requests library. Run pipenv install requests
# - Run pipenv shell in order to use this env
# - Run py _apitest.py

import sys
import json
from collections import namedtuple
import requests

# Variables

client_id = ''
secret_key = ''
blockchain = ''
hash = ''

# Statics

api_url_base = 'https://stampd.io/api/v2'
# api_url_base = 'http://dev.stampd.io/api/v2'

# Login to API service

login_request = requests.get(api_url_base + '/init?client_id=' + client_id + '&secret_key=' + secret_key)
login_json = login_request.json()
print(login_json)
# login_json['message']
# login_json['type']
# login_json['code']
# login_json['session_id']

if 'code' in login_json and login_json['code'] == 300:
    print('Logged in successfully')
else:
    print('Login failed, exiting')
    sys.exit()

# Post a hash

post_request = requests.post(api_url_base + '/hash',
                             data={
                                 'sess_id': login_json['session_id'],
                                 'blockchain': blockchain,
                                 'hash': hash,
                                 # 'meta_emails': '',
                                 # 'meta_notes': '',
                                 # 'meta_filename': '',
                                 # 'meta_category': '',
                             })
post_json = post_request.json()
print(post_json)
# post_json['message']
# post_json['type']
# post_json['code']
# post_json['stamps_remaining']

# Get a hash

get_request = requests.get(
    api_url_base + '/hash?hash=' + hash + '&blockchain=' + blockchain + '&sess_id=' + login_json['session_id'])
get_json = get_request.json()
print(get_json)
# get_json['message']
# get_json['type']
# get_json['code']
# get_json['txid']
