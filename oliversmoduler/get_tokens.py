import json
from urllib.parse import urlencode, urljoin
import requests
import os

def get_options():
    dir = os.path.dirname(os.path.abspath(__file__))

    with open(f'{dir}/options.json') as f:
        options = json.load(f)

    return options

# Mostly for remembering the options.
scopes = [ 'commercialsortapi/', 'searchapi/', 'sampleprojectswagger/' ]

def get_token(scope, verbose: bool = False, verify: bool = False):
    options = get_options()['Oidc']

    headers = {
        'content-type': 'application/x-www-form-urlencoded'
    }

    data = {
        'grant_type': 'client_credentials',
        'audience': scope,
        'client_id': options['client_id'],
        'client_secret': options['client_secret']
    }

    url = urljoin(options['authority'], 'connect/token')
    
    response = requests.post(url, 
        headers = headers,
        data = data, 
        verify=verify)

    content = response.json()

    if verbose: print('Got bearer token successfully!')

    return content['access_token']

if __name__ == '__main__':
    token = get_token('commercialsortapi/')
    print(token)
