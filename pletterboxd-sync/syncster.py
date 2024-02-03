import sys
import uuid

from loguru import logger
from plexapi import myplex

from api.letterboxd import LetterboxdClient
from api.plex import PlexWatchlistClient
from utils import constants

# TMDB == The Movie Database
# IMDB == Internet Movie Database

# Set up Logger
logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>", level="INFO")


def run():
    # Connect to plex
    app_name = "Pletterboxd"

    # Launch Plex Oauth
    client_uuid = str(uuid.uuid4())
    plex_headers = {
        'X-Plex-Client-Identifier': client_uuid,
        'X-Plex-Product': app_name,
        'X-Plex-Platform': 'Plex Web',
        'X-Plex-Device': 'Linux',
    }
    # Create Oauth url for user to click
    plex_login = myplex.MyPlexPinLogin(headers=plex_headers, oauth=True)
    oauth_url = plex_login.oauthUrl()
    print(f"Click this link to signin to plex: {oauth_url}")

    # Wait for user to do the Plex signin and retrieve token from there
    plex_login.run()
    plex_login.waitForLogin()

    # Create plex client with fresh token
    plex_client = PlexWatchlistClient(plex_login.token)

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
