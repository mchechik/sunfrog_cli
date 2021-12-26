import os
import sys
import requests
import logging

from connection_test import auth_ok

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(levelname)s %(asctime)s - %(message)s',
    handlers = [logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger()

API_DEV_URL='https://devapi.sunfrogsolutions.com'
SUNFROG_API_USER=os.getenv('SUNFROG_API_USER', None)
SUNFROG_API_KEY=os.getenv('SUNFROG_API_KEY', None)
SUNFROG_API_BASE_URL=os.getenv('SUNFROG_API_BASE_URL', API_DEV_URL)

def execute_api_call(endpoint, method, payload={}):
    if not auth_ok():
        raise Exception('Auth failed.')

    if method == 'GET':
        # Supports additional URL param's via dict in payload
        url = f'{SUNFROG_API_BASE_URL}/{endpoint}?user={SUNFROG_API_USER}&key={SUNFROG_API_KEY}'
        for key in payload:
            url += f'&{key}={payload[key]}'

        resp = requests.get(url)
        return validate_response(resp)
    elif method == 'POST':
        resp = requests.post(
            url=f'{SUNFROG_API_BASE_URL}/{endpoint}?user={SUNFROG_API_USER}&key={SUNFROG_API_KEY}',
            headers={'Content-Type': 'application/json'},
            json=payload
        )
        return validate_response(resp)
    else:
        raise Exception(f'Unsupported API method: {method}')

def validate_response(resp):
    if resp.status_code == 200:
        return resp.json()
    else:
        raise Exception(f'API request failed with status {resp.status_code} and message: {resp.json()["message"]}')