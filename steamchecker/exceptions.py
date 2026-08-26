class SteamError(Exception):
    pass


class APIError(SteamError):
    pass


class RateLimitError(SteamError):
    pass
