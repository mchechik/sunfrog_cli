import sys
import logging
import click

from api_client import execute_api_call

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(levelname)s %(asctime)s - %(message)s',
    handlers = [logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger()

@click.group()
def cli():
    pass

@cli.command('get_product')
@click.argument('public_art_id', required=False, type=int)
def get_product(public_art_id):
    ''' Get product(s) from Sunfrog.
        If public_art_id is set, then gets 1 product.
        Else gets all products
    '''
    product_resp = None
    if public_art_id:
        product_resp = execute_api_call(
            endpoint='product',
            method='GET', 
            payload={'publicArtId': public_art_id}
        )
    else:
        product_resp = execute_api_call(
            endpoint='product',
            method='GET'
        )

    print(product_resp)

if __name__ == '__main__':
    cli()