import click
from steamchecker.logger import get_logger
from steamchecker.parser import parse_profile_page
from steamchecker.storage import save_stats

logger = get_logger(__name__)

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
