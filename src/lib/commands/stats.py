from src.lib.queries.pokemon_queries import get_user_stats


def stats(**kwargs):
    username = kwargs.get("username", "testuser")
    return get_user_stats(username)
