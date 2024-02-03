from dataclasses import dataclass, field

import requests

from model.film import Film


@dataclass
class LetterboxdClient:
    username: str
    base_watchlist_url: str = "https://letterboxd-list-radarr.onrender.com"
    watchlist_url: str = field(init=False)

    # Must init attributes that depend on other attributes, here
    def __post_init__(self):
        self.watchlist_url = f"{self.base_watchlist_url}/{self.username.strip()}/watchlist/"

    def fetch_watchlist(self) -> list[Film]:
        """ Get the user's watchlist using the 3rd party tool

        Original project
        https://github.com/screeny05/letterboxd-list-radarr
        :rtype: dict

        """

        # Hit URL to grab json version of list
        raw_resp = requests.get(self.watchlist_url)

        # Raise exception if there was an HTTP status error
        raw_resp.raise_for_status()

        # Load payload into python dict
        payload = raw_resp.json()

        # For each response, convert to Film object
        ret = [Film(**item) for item in payload]

        return ret
