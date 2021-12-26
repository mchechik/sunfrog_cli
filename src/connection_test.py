import os
import sys
import requests
import logging

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

def auth_ok():
    if SUNFROG_API_USER == None:
        raise Exception('Must set env var: SUNFROG_API_USER')
    if SUNFROG_API_KEY == None:
        raise Exception('Must set env var: SUNFROG_API_KEY')
    if SUNFROG_API_BASE_URL == API_DEV_URL:
        logger.warning(f'Using dev API at {SUNFROG_API_BASE_URL}')

    resp = requests.get(f"{SUNFROG_API_BASE_URL}/auth?user={SUNFROG_API_USER}&key={SUNFROG_API_KEY}")
    return resp.status_code == 200
