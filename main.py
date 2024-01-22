import sys

from loguru import logger

from utils import constants
from api.letterboxd import LetterboxdClient
from api.plex import PlexClient

# TMDB == The Movie Database
# IMDB == Internet Movie Database

# Set up Logger
logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>", level="INFO")


def run():
    # Connect to plex
    plex_client = PlexClient(username=constants.PLEX_USERNAME,
                             password=constants.PLEX_PASSWORD,
                             two_factor_auth=constants.PLEX_2FA)

    # Get Letterboxd watchlist
    letterboxd_client = LetterboxdClient(constants.LETTERBOXD_USERNAME)
    source_watchlist = letterboxd_client.fetch_watchlist()

    for film in source_watchlist:
        # Add film from letterboxd to watchlist
        is_added = plex_client.add_movie_to_watchlist(title=film.title,
                                                      tmdb_id=film.id,
                                                      imdb_id=film.imdb_id)

        if is_added:
            logger.info(f"{film.title} was added to your plex watchlist")


if __name__ == '__main__':
    run()
