from src.lib.queries.pokemon_queries import (
    pokemon_market_set, get_market_listings)


def testcommand(**kwargs):
    pokemon_market_set()
    return get_market_listings()
