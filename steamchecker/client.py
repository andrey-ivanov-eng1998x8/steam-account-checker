import time
import httpx
from steamchecker.exceptions import APIError, RateLimitError


class SteamClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "[https://api.steampowered.com](https://api.steampowered.com)"

    def get(self, endpoint: str, params: dict | None = None):
        if params is None:
            params = {}
        params["key"] = self.api_key
        
        url = f"{self.base_url}/{endpoint}"
        for attempt in range(3):
            resp = httpx.get(url, params=params)
            if resp.status_code == 429:
                if attempt == 2:
                    raise RateLimitError("hit rate limit, giving up")
                time.sleep(2 * (attempt + 1))
                continue
            if resp.status_code >= 500:
                time.sleep(1)
                continue
            if resp.status_code != 200:
                raise APIError(f"steam api returned status {resp.status_code}")
            return resp.json()
        raise APIError("max retries exceeded")
