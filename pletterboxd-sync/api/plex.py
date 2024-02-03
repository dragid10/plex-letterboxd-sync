from dataclasses import dataclass, field

from loguru import logger
from plexapi.myplex import MyPlexAccount
from plexapi.video import Movie


@dataclass
class PlexWatchlistClient:
    token: str
    plex: MyPlexAccount = field(init=False)

    def __post_init__(self):
        self.plex = MyPlexAccount(token=self.token)

    def add_movie_to_watchlist(self, title: str, tmdb_id: int = None, imdb_id: str = None) -> bool:
        """ Given a film on the Letterboxd watchlist, attempt to add it to the Plex watchlist

        Args:
            title   (str):  Title of the film
            tmdb_id (int):  Unique ID of the film from The Movie Database (TMDB)
            imdb_id (str):  Unique ID of the film from Internet Movie Database (IMDB)

        Returns:
            bool: `True` is movie was successfully added to the plex watchlist, `False` otherwise

        """
        is_found: bool = False

        # Search Plex discover for the movie
        found_movie = self._search_movie(title, tmdb_id, imdb_id)
        try:
            # If the movie was successfully added, return True
            self.plex.addToWatchlist(found_movie)
            is_found = True
        except Exception as exc:
            logger.error(f"Failed to add to watchlist: {exc}")
        return is_found

    def _search_movie(self, title: str, tmdb_id: int = None, imdb_id: str = None) -> Movie:
        """ Search for a movie on Plex discover.

        Searching Plex Discover is better than searching the actual media server,
        because there's a chance that the movie isn't already on the server, or that it may not be released

        Args:
            title   (str):  Title of the film
            tmdb_id (int):  Unique ID of the film from The Movie Database (TMDB)
            imdb_id (str):  Unique ID of the film from Internet Movie Database (IMDB)

        Returns:
            Movie: Plex representation of the film found in Plex Discover

        """
        ret_film: Movie | None = None
        search_results = self.plex.searchDiscover(query=title, libtype='movie')

        # Try to match film by GUID
        for result in search_results:
            for guid in result.guids:
                # Try to see if either the IMDB ID or TMDB ID matches plex search result
                if imdb_id in guid.id:
                    ret_film = result
                    break

                if str(tmdb_id) in guid.id:
                    ret_film = result
                    break

            # If we've found a valid search result, there's no need to keep going through the rest of the results
            if ret_film is not None:
                break

        return ret_film
